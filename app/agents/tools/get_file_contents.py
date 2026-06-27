from langchain_core.tools import tool
from app.utils.repo_manager import repo_manager

@tool
def get_file_contents(file_path: str):
    """
    Get the full contents of a specific file in the repository.
    Use this when you need to see the complete file, not just chunks.
    """
    file_path = file_path.lstrip("/\\")
    full_path = repo_manager.get_repo_path() / file_path
    

    if not full_path.exists():
        return f"File not found: {file_path}"

    content = full_path.read_text(encoding="utf-8", errors="ignore")
    return content[:1500]