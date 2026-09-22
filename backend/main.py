from fastapi import FastAPI, UploadFile, File, HTTPException
from pathlib import Path
import shutil
from fastapi.middleware.cors import CORSMiddleware

from parsers.pdf_parser import pdf_text_extractor
from parsers.docx_parser import docx_text_extractor
from parsers.ppt_parser import extract_pptx_content
from parsers.ocr import extract_image_text
from agents.orchestrator import execute_task
from rag.ingestion import ingest_document
from rag.rag_agent import answer_question
from fastapi.responses import FileResponse

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "http://127.0.0.1:5173",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

allowed_files = {".pdf",".docx",".ppt",".pptx",".png",".jpg",".jpeg"}
UPLOAD_DIR = Path("uploads")
UPLOAD_DIR.mkdir(exist_ok=True)

@app.get("/")
def home():
    return {"message": "Multi-Agent Document AI is running"}

@app.post("/upload")
async def upload_file(file: UploadFile = File(...)):
    extension = Path(file.filename).suffix.lower()

    if extension not in allowed_files:
        raise HTTPException(
            status_code=400,
            detail=f"Unsupported file type: {extension}"
        )

    file_path = UPLOAD_DIR / file.filename

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    # Automatically ingest supported files
    try:
        if extension == ".pdf":
            parsed_data = pdf_text_extractor(str(file_path))

        elif extension == ".docx":
            parsed_data = docx_text_extractor(str(file_path))

        elif extension == ".pptx":
            parsed_data = extract_pptx_content(str(file_path))

        elif extension in [".png", ".jpg", ".jpeg"]:
            parsed_data = extract_image_text(str(file_path))

        else:
            parsed_data = None

        if parsed_data is not None:
            ingestion_result = ingest_document(
                parsed_data=parsed_data,
                document_id=file.filename
            )
        else:
            ingestion_result = {
                "status": "Uploaded but not indexed"
            }

    except Exception as e:
        print("INGESTION ERROR:", repr(e))

        ingestion_result = {
            "status": "Upload successful, ingestion failed",
            "error": str(e)
        }

    return {
        "message": "File uploaded successfully",
        "filename": file.filename,
        "file_type": extension,
        "path": str(file_path),
        "ingestion": ingestion_result
    }


@app.post("/ingest")
def ingest_file(filename: str):

    file_path = UPLOAD_DIR / filename

    if not file_path.exists():
        raise HTTPException(
            status_code=404,
            detail=f"File does not exist: {filename}"
        )

    extension = file_path.suffix.lower()

    # Parse the document
    if extension == ".pdf":

        parsed_data = pdf_text_extractor(
            str(file_path)
        )

    elif extension == ".docx":

        parsed_data = docx_text_extractor(
            str(file_path)
        )

    elif extension == ".pptx":

        parsed_data = extract_pptx_content(
            str(file_path)
        )

    elif extension in [".png", ".jpg", ".jpeg"]:

        parsed_data = extract_image_text(
            str(file_path)
        )

    else:

        raise HTTPException(
            status_code=400,
            detail="Unsupported file type for ingestion."
        )

    # Send parsed document to RAG pipeline
    result = ingest_document(
        parsed_data=parsed_data,
        document_id=filename
    )

    return {
        "message": "Document indexed successfully",
        "filename": filename,
        "result": result
    }

@app.post("/query")
def query_document(
    question: str,
    filename: str | None = None
):
    try:

        result = answer_question(
            question=question,
            document_id=filename
        )

        return result

    except Exception as e:

        print("QUERY ERROR:", repr(e))

        raise HTTPException(
            status_code=500,
            detail=str(e)
        )

@app.get("/parse/{filename}")
def parse_file(filename:str):
    file_path = UPLOAD_DIR / filename
    if not file_path.exists() :
        raise HTTPException(
            status_code= 400,
            detail= f" file does not exist : {filename}"
        )
    extension = file_path.suffix.lower()

    if extension == ".pdf" :
        res = pdf_text_extractor(str(file_path))
    elif extension ==".docx":
        res = docx_text_extractor(str(file_path))

    elif extension == ".pptx":

        res = extract_pptx_content(
            str(file_path)
        )
    elif extension =='.png' or extension == '.jpg' or extension =='jpeg':
        res = extract_image_text(str(file_path))

    else :
        raise HTTPException(
            status_code= 400,
            detail= " currently onlu support docx and pdfs"
        )
    return res

# @app.post("/process")
# def process_request(
#     request: str,
#     filename: str
# ):
#     file_path = UPLOAD_DIR / filename

#     if not file_path.exists():
#         raise HTTPException(
#             status_code=404,
#             detail=f"File does not exist: {filename}"
#         )

#     extension = file_path.suffix.lower()

#     if extension == ".pdf":

#         document_data = pdf_text_extractor(
#             str(file_path)
#         )

#         result = execute_task(
#             user_request=request,
#             document_data=document_data
#         )

#     elif extension == ".docx":

#         document_data = docx_text_extractor(
#             str(file_path)
#         )

#         result = execute_task(
#             user_request=request,
#             document_data=document_data
#         )

#     elif extension == ".pptx":
#         presentation_data = extract_pptx_content(str(file_path))

#         presentation_data["file_path"] = str(file_path)

#         result = execute_task(
#         user_request=request,
#         presentation_data=presentation_data
#     )

#     elif extension in [".png", ".jpg", ".jpeg"]:

#         image_data = extract_image_text(
#             str(file_path)
#         )

#         result = execute_task(
#             user_request=request,
#             document_data=image_data
#         )

#     else:

#         raise HTTPException(
#             status_code=400,
#             detail="This file type is not currently supported for processing."
#         )

#     return result

@app.post("/process")
def process_request(request: str, filename: str):

    try:
        print("PROCESS STARTED")
        print("Request:", request)
        print("Filename:", filename)

        file_path = UPLOAD_DIR / filename

        print("File path:", file_path)
        print("File exists:", file_path.exists())

        if not file_path.exists():
            raise HTTPException(
                status_code=404,
                detail=f"File does not exist: {filename}"
            )

        extension = file_path.suffix.lower()

        print("Extension:", extension)

        if extension == ".pptx":

            print("Parsing PPTX...")

            presentation_data = extract_pptx_content(
                str(file_path)
            )

            presentation_data["file_path"] = str(file_path)
            presentation_data["filename"] = filename

            print("File path added:")
            print(presentation_data.get("file_path"))

            print("Calling orchestrator...")

            result = execute_task(
                user_request=request,
                presentation_data=presentation_data
            )

            print("Orchestrator finished")

            return result

        else:
            raise HTTPException(
                status_code=400,
                detail="This test currently supports PPTX only."
            )

    except HTTPException:
        raise

    except Exception as e:

        print("ERROR:", repr(e))

        raise HTTPException(
            status_code=500,
            detail=str(e)
        )

@app.get("/download/{filename}")
def download_file(filename: str):
    file_path = Path("outputs") / filename

    if not file_path.exists():
        raise HTTPException(
            status_code=404,
            detail="File not found"
        )

    return FileResponse(
        path=str(file_path),
        filename=filename,
        media_type="application/octet-stream"
    )