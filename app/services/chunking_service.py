class ChunkingService:
    CHUNK_SIZE = 300
    CHUNK_OVERLAP = 50


    def chunk_documents(self, documents):
        chunks = []
        for document in documents:
            content = document["content"]

            for start in range(
                0,
                len(content),
                self.CHUNK_SIZE - self.CHUNK_OVERLAP
            ):
                chunk_content = content[
                start : start + self.CHUNK_SIZE
                ]
                chunk = {
                    "content": chunk_content,
                    "source": document["path"],
                    "start_index": start
                }

                chunks.append(chunk)
        return chunks
    

chunking_service = ChunkingService() 
