import os
import json
from pathlib import Path
from urllib.request import Request, urlopen
from dotenv import load_dotenv


# --------------------------------------------------
# Load .env from the backend directory
# --------------------------------------------------

BASE_DIR = Path(__file__).resolve().parents[1]
ENV_PATH = BASE_DIR / ".env"

load_dotenv(ENV_PATH)


# --------------------------------------------------
# Get LangSearch API key
# --------------------------------------------------

API_KEY = os.getenv("LANGSEARCH_API_KEY")

if not API_KEY:
    raise ValueError(
        f"LANGSEARCH_API_KEY not found.\n"
        f"Expected .env file at: {ENV_PATH}"
    )


# --------------------------------------------------
# Web Search
# --------------------------------------------------

def search_web(query: str, count: int = 5):

    request = Request(
        "https://api.langsearch.com/v1/web-search",
        data=json.dumps({
            "query": query,
            "count": count,
            "contents": {
                "text": True
            },
            "freshness": "noLimit"
        }).encode("utf-8"),
        headers={
            "Authorization": f"Bearer {API_KEY}",
            "Content-Type": "application/json"
        },
        method="POST"
    )

    try:

        with urlopen(request, timeout=30) as response:
            result = json.load(response)

    except Exception as e:
        raise RuntimeError(
            f"LangSearch request failed: {str(e)}"
        )


    # --------------------------------------------------
    # Extract useful information from search response
    # --------------------------------------------------

    sources = []

    web_pages = (
        result
        .get("data", {})
        .get("webPages", {})
        .get("value", [])
    )

    for item in web_pages:

        sources.append({
            "title": item.get("name", ""),
            "url": item.get("url", ""),
            "content": (
                item.get("snippet")
                or item.get("text")
                or ""
            )
        })

    return sources