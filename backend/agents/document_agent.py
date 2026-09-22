from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from agents.schemas import DocumentAnalysis
import os
load_dotenv()

model = ChatOpenAI(
    model="nvidia/nemotron-3-super-120b-a12b",
    api_key=os.getenv("NVIDIA_API_KEY"),
    base_url="https://integrate.api.nvidia.com/v1",
    temperature=0
)

structured_model = model.with_structured_output(
    DocumentAnalysis
)


def analyze_doc(document_data : dict):

    prompt = f"""
You are a document analysis agent.

Analyze the following extracted document information.

DOCUMENT DATA:
{document_data}

Return a structured analysis containing:

1. document_type
2. purpose
3. tone
4. sections
5. important_content
6. style

For style, identify information available from the
provided document data, such as heading styles,
paragraph styles, fonts, and formatting.

Do not invent information that is not present.

Return the result as JSON.

"""
    response = structured_model.invoke(prompt)
    return response

