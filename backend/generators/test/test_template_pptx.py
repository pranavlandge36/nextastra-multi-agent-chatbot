from agents.research_agent import research_topic
from generators.template_pptx_generator import (
    generate_pptx_from_template
)


research = research_topic(
    "Latest developments in generative AI"
)


file_path = generate_pptx_from_template(
    research_result=research,
    template_path="uploads/1.pptx",
    filename="template_based_report.pptx"
)


print("Generated:", file_path)