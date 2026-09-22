from rag.indexer import index_document


text = """
Artificial intelligence is transforming many industries.

Generative AI can create text, images, code and other
forms of content.

Retrieval augmented generation combines language models
with external knowledge sources.

A RAG system retrieves relevant information from a
knowledge base before generating an answer.
""" * 10


result = index_document(
    text=text,
    document_id="test-document"
)

print(result)