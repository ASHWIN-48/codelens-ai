from fastapi import APIRouter
from pydantic import BaseModel
from app.services.agent_service import agent_service

router = APIRouter()

class AskRequest(BaseModel):
    question: str

@router.post("/ask")
def ask_question(request: AskRequest):
    result = agent_service.run(request.question)
    return {"answer": result}