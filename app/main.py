from fastapi import FastAPI
from app.core.config import settings
from app.api.chat import router as chat_router

app = FastAPI(
    title=settings.APP_NAME,
    version="1.0.0"
)

app.include_router(
    chat_router,
    prefix="/chat",
    tags=["chat"]
)

@app.get("/")
async def root():
    return {
        "app": settings.APP_NAME,
        "environment": settings.ENVIRONMENT
    }

@app.get("/health")
async def health():
    return {
        "status": "healthy"
    }