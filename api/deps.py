from typing import Any, AsyncGenerator

from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from database import session_maker
from services.messages import MessagesService


async def get_session() -> AsyncGenerator[Any, AsyncSession]:
    async with session_maker() as session:
        yield session


async def get_messages_service(
    session: AsyncSession = Depends(get_session),
) -> MessagesService:
    return MessagesService(session=session)
