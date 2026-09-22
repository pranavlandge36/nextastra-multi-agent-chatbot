from rag.embedding import create_embeddings, create_query_embedding


texts = [
    "Artificial intelligence is transforming industries.",
    "Generative AI can create text, images and code.",
    "Retrieval augmented generation uses external knowledge."
]


vectors = create_embeddings(texts)

print("Number of vectors:", len(vectors))
print("Vector dimension:", len(vectors[0]))

query_vector = create_query_embedding(
    "What is generative AI?"
)

print("Query vector dimension:", len(query_vector))