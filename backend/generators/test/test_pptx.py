from agents.research_agent import research_topic
from generators.pptx_generator import generate_pptx


research = research_topic(
    "Latest developments in generative AI"
)


file_path = generate_pptx(
    research,
    "generative_ai_report.pptx"
)


print("Generated:", file_path)