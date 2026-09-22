from rag.chunking import chunk_text


text = """
Artificial intelligence is transforming many industries.
Generative AI can create text, images, code and other content.
Retrieval augmented generation combines language models
with external knowledge sources. This allows applications
to answer questions using specific documents.
""" * 20


chunks = chunk_text(text)

print("Number of chunks:", len(chunks))

for i, chunk in enumerate(chunks):
    print(f"\n--- Chunk {i + 1} ---")
    print(chunk[:300])