from pydantic import BaseModel
from typing import Optional

class QueryRequest(BaseModel):
    query: str
    model: Optional[str] = "gpt-4o"

class QueryResponse(BaseModel):
    response: str