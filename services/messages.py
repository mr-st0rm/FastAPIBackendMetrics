import structlog
from fastapi import HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import status

from api.v1.schemas.message import MessageOut
from repositories.message import MessageRepo


logger = structlog.get_logger()


class MessagesService:
    def __init__(self, session: AsyncSession):
        self.message_repo = MessageRepo(session)

    async def __get_message_or_404(self, message_id: int) -> MessageOut:
        message = await self.message_repo.get_message_by_id(message_id)
        if not message:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Message with id {message_id} not found",
            )
        return MessageOut.model_validate(message)

    async def get_message_text(self, message_id: int) -> str:
        message = await self.__get_message_or_404(message_id)

        logger.info("Read message text for message with id %s", message_id)

        return message.text
