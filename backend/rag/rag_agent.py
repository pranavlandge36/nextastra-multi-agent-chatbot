import os

from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

from rag.retriever import search_similar_chunks


load_dotenv()


model = ChatOpenAI(
    model="nvidia/nemotron-3-super-120b-a12b",
    api_key=os.getenv("NVIDIA_API_KEY"),
    base_url="https://integrate.api.nvidia.com/v1",
    temperature=0
)


def answer_question(
    question: str,
    top_k: int = 3,
    document_id: str | None = None
):

    # Retrieve relevant chunks
    results = search_similar_chunks(
    query=question,
    top_k=top_k,
    document_id=document_id
)

    context = "\n\n".join(
        result["text"]
        for result in results
    )

    prompt = f"""
You are a document question-answering assistant.

Answer the user's question using ONLY the supplied context.

If the answer cannot be found in the context,
say that the information is not available in the
provided documents.

CONTEXT:
{context}

QUESTION:
{question}

Give a clear and concise answer.
"""

    response = model.invoke(prompt)

    return {
        "question": question,
        "answer": response.content,
        "sources": [
            {
                "document_id": result["document_id"],
                "chunk_index": result["chunk_index"],
                "score": result["score"]
            }
            for result in results
        ]
    }