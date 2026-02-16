from fastapi import HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import status

from repositories.message import MessageRepo


class MessagesService:
    def __init__(self, session: AsyncSession):
        self.message_repo = MessageRepo(session)

    async def get_message_text(self, message_id: int) -> str:
        message = await self.message_repo.get_message_by_id(message_id)

        if not message:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Message with id {message_id} not found",
            )

        return message.text
