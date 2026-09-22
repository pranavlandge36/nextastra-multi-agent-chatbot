from agents.document_agent import analyze_doc


sample_document = {
    "file_type": "docx",
    "paragraph_count": 5,
    "paragraphs": [
        {
            "text": "Company Proposal",
            "style": "Title"
        },
        {
            "text": "Executive Summary",
            "style": "Heading 1"
        },
        {
            "text": "Our company provides AI solutions.",
            "style": "Normal"
        },
        {
            "text": "Problem Statement",
            "style": "Heading 1"
        },
        {
            "text": "Businesses face challenges adopting AI.",
            "style": "Normal"
        }
    ]
}


result = analyze_doc(sample_document)

print(result)
print(type(result))