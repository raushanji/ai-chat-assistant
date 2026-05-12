from fastapi import Request
from fastapi.responses import JSONResponse

from app.core.exceptions import AIServiceException


async def ai_exception_handler(
    request: Request,
    exc: AIServiceException
):

    return JSONResponse(
        status_code=500,
        content={
            "error": exc.message
        }
    )