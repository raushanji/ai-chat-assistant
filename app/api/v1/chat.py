from fastapi import APIRouter
from app.services.chat_service import ChatService
from app.schemas.chat import ChatRequest

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