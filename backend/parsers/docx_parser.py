from docx import Document

def docx_text_extractor(file_path : str):

    doc = Document(file_path)

    paras = []

    for para in doc.paragraphs :
        text = para.text.strip()

        if text :
            paras.append({
                'text' : text,
                "style" : para.style.name
            })

    return {
        "file_type": "docx",
        "paragraph_count": len(paras),
        "paragraphs": paras
    }