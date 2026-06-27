import faiss
import numpy as np
import json
import os
from app.core.config import settings

class RetrieverService:
    def build_index(self, chunks):
        embeddings = [chunk["embedding"] for chunk in chunks]
        embeddings = np.array(embeddings, dtype="float32")
        dimension = len(embeddings[0])
        self.index = faiss.IndexFlatL2(dimension)
        self.index.add(embeddings)
        self.chunks = chunks


    def save_index(self):
        faiss.write_index(self.index, settings.FAISS_INDEX_PATH)

        clean_chunks = [
            {
                "content": chunk["content"],
                "source": chunk["source"],
                "start_index": chunk["start_index"]
            }
            for chunk in self.chunks
        ]

        with open(settings.CHUNKS_PATH, "w") as f:
            json.dump(clean_chunks, f)


    def load_index(self):
        if os.path.exists(settings.FAISS_INDEX_PATH) and os.path.exists(settings.CHUNKS_PATH):
            self.index = faiss.read_index(settings.FAISS_INDEX_PATH)

            with open(settings.CHUNKS_PATH, "r") as f:
                self.chunks = json.load(f)

            print("FAISS index loaded from disk")
        else:
            print("No saved index found")


    def retrieve(self, query_embedding, top_k=5):
        if not hasattr(self, "index"):
            return "No repository indexed yet. Please ingest a repository first."

        distances, indices = self.index.search(query_embedding, top_k)
        results = [self.chunks[i] for i in indices[0]]
        return results

retriever_service = RetrieverService()    
        
          