testset = [
    {
        "question": "What embedding model does Parchment use?",
        "ground_truth": "Parchment uses all-MiniLM-L6-v2 from SentenceTransformer for generating embeddings."
    },
    {
        "question": "How does Parchment persist the FAISS index?",
        "ground_truth": "Parchment saves the FAISS index as bytes into MongoDB Atlas, keyed by session_id, along with chunk_ids as pickled bytes."
    },
    {
        "question": "What is the chunking strategy in Parchment?",
        "ground_truth": "Parchment chunks PDFs into 500 character chunks with 50 character overlap."
    },
    {
        "question": "What reranking model does Parchment use?",
        "ground_truth": "Parchment uses cross-encoder/ms-marco-MiniLM-L-6-v2 as its cross-encoder reranker."
    },
    {
        "question": "How does confidence thresholding work in Parchment?",
        "ground_truth": "If the top reranked chunk score is below MIN_CONFIDENCE threshold, Parchment returns 'I don't have enough information to answer this.' instead of generating an answer."
    },
    {
        "question": "What LLM does Parchment use for answer generation?",
        "ground_truth": "Parchment uses Groq API with llama-3.1-8b-instant model for answer generation."
    },
    {
        "question": "How does session isolation work in Parchment?",
        "ground_truth": "Each session gets its own FAISS index stored in MongoDB with a unique session_id so documents don't mix between different users."
    },
    {
        "question": "What is the deployment stack for Parchment?",
        "ground_truth": "Parchment backend is deployed on Railway and frontend is deployed on Vercel at parchment-gamma.vercel.app."
    },
    {
        "question": "What does the rerank function do in retrieval.py?",
        "ground_truth": "It takes query and chunks, scores each query-chunk pair using the cross-encoder predict method, applies sigmoid normalization, and returns chunks sorted by score descending."
    },
    {
        "question": "What database does Parchment use and for what?",
        "ground_truth": "Parchment uses MongoDB Atlas for storing document metadata, chunks, and FAISS index bytes per session."
    }
]