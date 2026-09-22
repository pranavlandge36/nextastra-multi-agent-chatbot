from agents.ppt_agent import analyze_presentation


sample_presentation = {
    "file_type": "pptx",
    "slide_count": 3,
    "slides": [
        {
            "slide_number": 1,
            "layout": "Title Slide",
            "texts": [
                "Company Overview"
            ],
            "fonts": [
                "Aptos Display"
            ],
            "images": 1
        },
        {
            "slide_number": 2,
            "layout": "Title and Content",
            "texts": [
                "Our Product",
                "AI-powered platform for businesses"
            ],
            "fonts": [
                "Aptos"
            ],
            "images": 1
        },
        {
            "slide_number": 3,
            "layout": "Two Content",
            "texts": [
                "Market Opportunity",
                "Growing enterprise AI adoption"
            ],
            "fonts": [
                "Aptos"
            ],
            "images": 0
        }
    ]
}


result = analyze_presentation(sample_presentation)

print(result)

print("\nType:")
print(type(result))

print("\nDictionary:")
print(result.model_dump())