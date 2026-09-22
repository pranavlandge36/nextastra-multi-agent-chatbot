from rag.chunking import chunk_text
from rag.embedding import create_embeddings
from rag.pinecone_store import get_index


def index_document(
    text: str,
    document_id: str
):
    # 1. Split document into chunks
    chunks = chunk_text(text)

    # 2. Create embeddings
    vectors = create_embeddings(chunks)

    # 3. Get Pinecone index
    index = get_index()

    # 4. Prepare vectors
    records = []

    for i, (chunk, vector) in enumerate(zip(chunks, vectors)):

        records.append({
            "id": f"{document_id}-{i}",
            "values": vector,
            "metadata": {
                "document_id": document_id,
                "chunk_index": i,
                "text": chunk
            }
        })

    # 5. Upload to Pinecone
    index.upsert(vectors=records)

    return {
        "document_id": document_id,
        "chunks_indexed": len(records)
    }