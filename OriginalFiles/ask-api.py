from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional
from openai import OpenAI
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Create FastAPI app instance
app = FastAPI()

# Initialize OpenAI client (it will automatically use OPENAI_API_KEY from environment)
client = OpenAI()

# Define request/response models
class QueryRequest(BaseModel):
    query: str
    model: Optional[str] = "gpt-3.5-turbo"

class QueryResponse(BaseModel):
    response: str

# Create test routes
@app.post("/api/query", response_model=QueryResponse)
async def process_query(request: QueryRequest):
    try:
        # Here you can add your existing ClinicalMindSidekick logic
        # For testing purposes, we'll return a mock response
        completion = client.chat.completions.create(
            model=request.model,
            store=True,
            messages=[
        {"role": "system", "content": "You are a helpful assistant that can answer questions and help with tasks."},
        {"role": "user", "content": request.query},
        {"role": "assistant", "content": "I'm here to help. What specific concerns do you have about Karen? Is it related to risk, treatment effectiveness, or another area?"}
    ]
        )
        return {"response": f"{completion.choices[0].message.content}"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


