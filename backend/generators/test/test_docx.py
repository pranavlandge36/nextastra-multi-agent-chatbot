from agents.research_agent import research_topic
from generators.docx_generator import generate_docx


# Get research
research = research_topic(
    "Latest developments in generative AI"
)


# Generate DOCX
file_path = generate_docx(
    research,
    "generative_ai_report.docx"
)


print("Generated:", file_path)