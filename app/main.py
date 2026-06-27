
from dotenv import load_dotenv
load_dotenv()
from contextlib import asynccontextmanager
from fastapi import FastAPI
from app.core.config import settings
from app.api.routes.ingest import router as ingest_router
from app.api.routes.ask import router as ask_router
from app.services.retrieval_service import retriever_service
import logging
import os
from app.utils.repo_manager import repo_manager
from pathlib import Path
from app.core.config import settings
from app.api.routes.generate_docs import router as generate_docs_router


logger = logging.getLogger(__name__)


@asynccontextmanager
async def lifespan(app:FastAPI):
    print("Starting CodeLens AI Service")
    logger.info("Starting CodeLens AI Service")
    repo_manager.current_repo_path = Path(settings.REPO_STORAGE_PATH)
    retriever_service.load_index()

    yield

    print("Shutting down CodeLens AI Service")


app=FastAPI(
    title=settings.APP_NAME,
    lifespan=lifespan
)

app.include_router(ingest_router)
app.include_router(ask_router)
app.include_router(generate_docs_router)


@app.get("/health")
def health_check():
    return{
        "status":"healthy"
    }