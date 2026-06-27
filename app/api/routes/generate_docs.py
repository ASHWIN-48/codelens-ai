from fastapi import APIRouter
from pydantic import BaseModel
from app.services.agent_service import agent_service

router = APIRouter()

class DocsRequest(BaseModel):
    file_path: str

@router.post("/generate-docs")
def generate_docs(request: DocsRequest):
    task = f"""You are a documentation generator for a code repository.

Call get_file_contents with file_path="{request.file_path}" to read the file.
Then for each function and class you can actually see in the file, call get_function_definition to read it fully.
Write clean markdown documentation for each one: what it does, parameters, return value, notes.

Only document functions that actually exist in the file. Do not invent any."""
    result = agent_service.run(task)
    return {"file_path": request.file_path, "documentation": result}