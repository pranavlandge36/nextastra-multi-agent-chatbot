from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

from agents.schemas import ResearchResult
from research.web_search import search_web
import os

load_dotenv()


# --------------------------------------------------
# LLM
# --------------------------------------------------

model = ChatOpenAI(
    model="nvidia/nemotron-3-super-120b-a12b",
    api_key=os.getenv("NVIDIA_API_KEY"),
    base_url="https://integrate.api.nvidia.com/v1",
    temperature=0
)


structured_model = model.with_structured_output(ResearchResult)


# --------------------------------------------------
# Research Agent
# --------------------------------------------------

def research_topic(topic: str) -> ResearchResult:

    # 1. Search the web
    search_results = search_web(topic, count=5)

    # 2. Give real search results to the LLM
    prompt = f"""
You are a research analysis agent.

Research topic:
{topic}

The following information was retrieved from a web search API.

SEARCH RESULTS:
{search_results}

Your job is to analyze these search results and produce a
structured research report.

IMPORTANT RULES:

1. Use the supplied search results as your factual source.
2. Do not invent URLs.
3. Do not invent sources.
4. Do not claim information that is not supported by the
   supplied search results.
5. Include the most relevant sources.
6. Keep the summary concise but informative.

Return:
- topic
- summary
- key_findings
- sources
"""

    # 3. Generate structured result
    response = structured_model.invoke(prompt)

    return response