import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

from generators.docx_generator import generate_docx
from generators.pptx_generator import generate_pptx

load_dotenv()

model = ChatOpenAI(
    model="nvidia/nemotron-3-super-120b-a12b",
    api_key=os.getenv("NVIDIA_API_KEY"),
    base_url="https://integrate.api.nvidia.com/v1",
    temperature=0
)


def generate_output(research_result, output_format="docx"):
    """
    Generate a document or presentation from a ResearchResult.
    """

    if output_format.lower() == "docx":
        return generate_docx(research_result)

    elif output_format.lower() == "pptx":
        return generate_pptx(research_result)

    else:
        raise ValueError(
            f"Unsupported output format: {output_format}"
        )