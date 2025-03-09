from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from clinical_mind_sidekick.api.routes import router

# Create FastAPI app - this needs to be at module level, not inside a function
app = FastAPI(
    title="Clinical Mind Sidekick",
    description="API for mental health consultation",
    version="1.0.0"
)

# Configure CORS
origins = [
    "http://localhost:4200",  # Angular development server
    "https://main.da1yk2y8qhshn.amplifyapp.com",  # Placeholder for production URL
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include the router
app.include_router(router, prefix="/api")

# This is optional - only needed if you're running the file directly
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)