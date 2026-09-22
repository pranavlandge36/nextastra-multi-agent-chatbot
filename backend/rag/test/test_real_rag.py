from rag.rag_agent import answer_question


result = answer_question(
    "What are the different types of wind turbine generators?"
)

print("\nANSWER:")
print(result["answer"])

print("\nSOURCES:")

for source in result["sources"]:
    print(source)