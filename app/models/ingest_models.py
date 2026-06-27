from pydantic import BaseModel


class IngestRequest(BaseModel):
    repo_url: str