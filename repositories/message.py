from sqlalchemy import select

from database.models import Message
from repositories.base import BaseRepository


class MessageRepo(BaseRepository):
    async def get_message_by_id(self, message_id: int) -> Message | None:
        statement = select(Message).where(Message.id == message_id)
        return await self.session.scalar(statement)
