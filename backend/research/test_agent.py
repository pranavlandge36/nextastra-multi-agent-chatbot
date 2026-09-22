from agents.research_agent import research_topic


result = research_topic(
    "Latest developments in generative AI"
)

print("\nTOPIC:")
print(result.topic)

print("\nSUMMARY:")
print(result.summary)

print("\nKEY FINDINGS:")

for finding in result.key_findings:
    print("-", finding)

print("\nSOURCES:")

for source in result.sources:
    print("-", source.title)
    print(" ", source.url)
    print(" ", source.relevance)