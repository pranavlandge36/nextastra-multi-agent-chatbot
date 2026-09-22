from rag.pinecone_store import get_index


index = get_index()

print("Pinecone connected successfully!")

print(
    index.describe_index_stats()
)