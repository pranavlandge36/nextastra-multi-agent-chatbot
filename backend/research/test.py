from research.web_search import search_web

results = search_web("latest AI trends 2026")

for result in results:
    print(result["title"])
    print(result["url"])
    print()