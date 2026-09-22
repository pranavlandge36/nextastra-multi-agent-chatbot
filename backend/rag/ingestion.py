from rag.normalizer import normalize_document
from rag.indexer import index_document


def ingest_document(
    parsed_data,
    document_id: str
):
    # Convert parser output into plain text
    text = normalize_document(parsed_data)

    if not text.strip():
        raise ValueError("Document contains no usable text.")

    # Chunk + embed + store in Pinecone
    result = index_document(
        text=text,
        document_id=document_id
    )

    return result