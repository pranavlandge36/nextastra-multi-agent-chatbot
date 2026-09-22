from pypdf import PdfReader

def pdf_text_extractor(file_path : str):
    reader = PdfReader(file_path)

    pages = []

    for page_num , page in enumerate(reader.pages, start=1):
        text = page.extract_text() or ""

        pages.append({
            "page" : page_num,
            "text" : text
        })
    return {
        'file_type' : 'pdf',
        'page_count' : len(pages),
        "pages" : pages
    }