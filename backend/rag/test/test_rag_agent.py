from rag.rag_agent import answer_question


result = answer_question(
    "What is retrieval augmented generation?"
)


print("\nANSWER:")
print(result["answer"])


print("\nSOURCES:")

for source in result["sources"]:
    print(source)