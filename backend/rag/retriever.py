from rag.embedding import create_query_embedding
from rag.pinecone_store import get_index


def search_similar_chunks(
    query: str,
    top_k: int = 3,
    document_id: str | None = None
):
    index = get_index()

    query_vector = create_query_embedding(query)

    query_args = {
    "vector": query_vector,
    "top_k": top_k,
    "include_metadata": True
}

    if document_id:
        query_args["filter"] = {
        "document_id": {
            "$eq": document_id
        }
    }

    results = index.query(**query_args)

    chunks = []

    for match in results["matches"]:
        chunks.append({
            "id": match["id"],
            "score": match["score"],
            "text": match["metadata"].get("text", ""),
            "document_id": match["metadata"].get("document_id"),
            "chunk_index": match["metadata"].get("chunk_index")
        })

    return chunks

# def search_similar_chunks(query: str, top_k: int = 10, document_id: str | None = None):
#     index = get_index()
#     query_vector = create_query_embedding(query)

#     query_args = {
#         "vector": query_vector,
#         "top_k": top_k,
#         "include_metadata": True
#     }

#     if document_id:
#         query_args["filter"] = {
#             "document_id": {
#                 "$eq": document_id
#             }
#         }

#     results = index.query(**query_args)

#     chunks = []

#     for match in results["matches"]:
#         print("\n--- MATCH ---")
#         print("ID:", match["id"])
#         print("Score:", match["score"])
#         print("Document:", match["metadata"].get("document_id"))
#         print("Chunk:", match["metadata"].get("chunk_index"))
#         print("TEXT:")
#         print(match["metadata"].get("text", ""))

#         chunks.append({
#             "id": match["id"],
#             "score": match["score"],
#             "text": match["metadata"].get("text", ""),
#             "document_id": match["metadata"].get("document_id"),
#             "chunk_index": match["metadata"].get("chunk_index")
#         })

#     return chunks