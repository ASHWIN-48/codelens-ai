from fastapi import APIRouter

from app.models.ingest_models import IngestRequest
from app.services.github_service import github_service


router = APIRouter()


@router.post("/ingest")
def ingest_repo(request: IngestRequest):
    return {
        "repo_url": request.repo_url
    }

@router.post("/github")
async def ingest_github_repo(request: IngestRequest):

    result = await github_service.ingest_repository(
        request.repo_url
    )

    return result