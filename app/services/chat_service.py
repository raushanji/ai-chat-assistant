import asyncio
import logging

from ollama import chat

logger = logging.getLogger(__name__)


class ChatService:

    async def ask(self, message: str):

        try:

            response = await asyncio.wait_for(
                asyncio.to_thread(
                    chat,
                    model="tinyllama",
                    messages=[
                        {
                            "role": "user",
                            "content": message
                        }
                    ]
                ),
                timeout=30
            )

            return response["message"]["content"]

        except asyncio.TimeoutError:

            logger.error("Ollama request timed out")

            return "Request timed out. Please try again."

        except Exception as e:

            logger.exception(e)

            return "Something went wrong."