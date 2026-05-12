from fastapi import APIRouter
from app.services.chat_service import ChatService
from app.schemas.chat import ChatRequest
from fastapi.responses import StreamingResponse

import asyncio

router = APIRouter()

chat_service = ChatService()

@router.post("/")
async def chat_endpoint(request: ChatRequest):

    response = await chat_service.ask(
        request.message
    )

    return {
        "response": response
    }


async def fake_stream():

    words = [
        "Hello",
        " this",
        " is",
        " streaming"
    ]

    for word in words:

        yield word

        await asyncio.sleep(0.5)

@router.get("/stream")
async def stream():

    return StreamingResponse(
        fake_stream(),
        media_type="text/plain"
    )