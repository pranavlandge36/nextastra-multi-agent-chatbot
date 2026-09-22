from rag.retriever import search_similar_chunks


results = search_similar_chunks(
    "What is retrieval augmented generation?",
    top_k=3
)

for result in results:

    print("\n--------------------")

    print("Score:", result["score"])

    print("Document:", result["document_id"])

    print("Chunk:", result["chunk_index"])

    print("Text:", result["text"])