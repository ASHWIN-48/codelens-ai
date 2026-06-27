from app.services.embedding_service import embedder_service
from app.services.retrieval_service import retriever_service
from langchain_core.tools import tool


@tool
def search_codebase(query: str):
    """
    Search the codebase for relevant code chunks based on a query.
    Returns matching code with file sources.
    """
    query_embedding = embedder_service.embed_query(query)
    results = retriever_service.retrieve(
        query_embedding=query_embedding,
        top_k=3
    )

    if isinstance(results, str):
        return results

    formatted = "\n\n".join([
    f"File: {r['source']}\n{r['content'][:300]}"
    for r in results
])

    return formatted