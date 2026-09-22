from parsers.ppt_parser import extract_pptx_content
from rag.ingestion import ingest_document


parsed_data = extract_pptx_content(
    "uploads/1.pptx"
)

result = ingest_document(
    parsed_data=parsed_data,
    document_id="wind-turbine-presentation"
)

print(result)