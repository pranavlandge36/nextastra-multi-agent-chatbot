from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
import os
from agents.schemas import PPTAnalysis


load_dotenv()
api_key = os.getenv("NVIDIA_API_KEY")

# model = ChatOpenAI(
#     model="nvidia/nemotron-3-super-120b-a12b:free",
#     api_key=os.getenv("OPENROUTER_API_KEY"),
#     base_url="https://openrouter.ai/api/v1",
#     temperature=0
# )
model = ChatOpenAI(
    model="nvidia/nemotron-3-super-120b-a12b",
    api_key=api_key,
    base_url="https://integrate.api.nvidia.com/v1",
    temperature=0
)


structured_model = model.with_structured_output(
    PPTAnalysis
)


def analyze_presentation(presentation_data: dict) -> PPTAnalysis:

    prompt = f"""
You are a PowerPoint presentation analysis agent.

Analyze the following extracted PowerPoint information.

PRESENTATION DATA:
{presentation_data}

Determine:

1. What type of presentation this is
2. Its main purpose
3. Its overall tone
4. The purpose of each slide
5. Important content on each slide
6. The layouts used
7. The fonts used
8. The overall visual style

Only use information available in the provided data.
Do not invent specific facts.

Return the result using the required structured schema.
"""

    response = structured_model.invoke(prompt)

    return response