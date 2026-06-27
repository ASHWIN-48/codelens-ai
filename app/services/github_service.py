from app.utils.repo_manager import repo_manager
from app.utils.file_filters import FileLoader
from app.services.chunking_service import chunking_service
from app.services.embedding_service import embedder_service
from app.services.retrieval_service import retriever_service
from app.services.generator_service import generator_service


file_loader = FileLoader()




class GithubService:
    async def ingest_repository(self, repo_url: str):
        repo_path = repo_manager.clone_repository(repo_url)
        documents = file_loader.load_repository_files(repo_path)
        chunks = chunking_service.chunk_documents(documents)
    

        embedded_chunks=embedder_service.embed_chunks(chunks)
        

        retriever_service.build_index(embedded_chunks)
        retriever_service.save_index()
        
        return {
    "repo_path": str(repo_path),
    "documents": len(documents),
    "chunks": len(chunks)
    
    
}
    
    
github_service = GithubService()