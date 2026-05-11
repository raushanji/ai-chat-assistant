from fastapi import FastAPI

app = FastAPI(
    title="AI Chat Assistant",
    version="1.0.0"
)

@app.get("/")
async def root():
    return {
        "message": "AI Chat Assistant Running"
    }

@app.get("/health")
async def health():
    return {
        "status": "healthy"
    }