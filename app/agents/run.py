from dotenv import load_dotenv
load_dotenv()

from app.agents.graph import graph
from app.services.retrieval_service import retriever_service
from app.utils.repo_manager import repo_manager
from pathlib import Path
from app.core.config import settings

repo_manager.current_repo_path = Path(settings.REPO_STORAGE_PATH)
retriever_service.load_index()

result = graph.invoke({
    "question": "How authentication works?",
    "messages": []
})

print(result)