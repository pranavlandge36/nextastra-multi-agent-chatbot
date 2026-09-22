from parsers.ppt_parser import extract_pptx_content
from rag.normalizer import normalize_document


data = extract_pptx_content(
    "uploads/1.pptx"
)

text = normalize_document(data)

print("Normalized text:\n")
print(text[:3000])