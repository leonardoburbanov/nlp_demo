from fastapi import FastAPI
from typing import Dict, Any

# Create FastAPI instance
app = FastAPI(
    title="NLP Demo API",
    description="A simple FastAPI backend for NLP demo",
    version="0.1.0"
)


@app.get("/")
async def root() -> Dict[str, str]:
    """
    Root endpoint that returns a welcome message.
    
    Returns:
        Dict[str, str]: A welcome message
    """
    return {"message": "Welcome to NLP Demo API!"}


@app.get("/health")
async def health_check() -> Dict[str, str]:
    """
    Health check endpoint to verify the API is running.
    
    Returns:
        Dict[str, str]: Health status
    """
    return {"status": "healthy", "service": "nlp-demo-api"}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
