from fastapi import FastAPI
from app.core.config import settings
from app.middleware.logging import LoggingMiddleware
from app.api.v1.router import api_router
from app.core.handlers import ai_exception_handler
from app.core.exceptions import AIServiceException

app = FastAPI(
    title=settings.APP_NAME,
    version="1.0.0"
)

app.add_middleware(LoggingMiddleware)
app.add_exception_handler(
    AIServiceException,
    ai_exception_handler
)

app.include_router(
    api_router,
    prefix="/api/v1"
)

# @app.get("/")
# async def root():
#     return {
#         "app": settings.APP_NAME,
#         "environment": settings.ENVIRONMENT
#     }

# @app.get("/health")
# async def health():
#     return {
#         "status": "healthy"
#     }