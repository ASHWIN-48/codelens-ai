from sentence_transformers import SentenceTransformer

class EmbedderService:
    def __init__(self):
        self.model = SentenceTransformer(
            "all-MiniLM-L6-v2"
            )
        
    def embed_chunks(self, chunks):
        chunk_texts = [chunk["content"] for chunk in chunks]
        print("starting embeddings")
        embeddings = self.model.encode(chunk_texts)
        print("embeddings done")
        for chunk, embedding in zip(chunks, embeddings):
            chunk["embedding"] = embedding.tolist()

        return chunks


    def embed_query(self, query: str):
        embedding = self.model.encode(query)
        embedding = embedding.reshape(1, -1)

        return embedding   

embedder_service=EmbedderService()            

