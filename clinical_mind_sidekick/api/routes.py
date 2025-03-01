from fastapi import APIRouter, HTTPException
from ..core.openai_client import get_openai_client
from .models import QueryRequest, QueryResponse
from ..services.ai_service import process_ai_query

router = APIRouter()

@router.get("/")
async def root():
    return {"message": "Welcome to Clinical Mind Sidekick API"}

@router.post("/query", response_model=QueryResponse)
async def process_query(request: QueryRequest):
    try:
        response = await process_ai_query(request.query, request.model)
        return {"response": response}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))