from typing import Any, AsyncGenerator

from sqlalchemy.ext.asyncio import AsyncSession

from database import session_maker


async def get_session() -> AsyncGenerator[Any, AsyncSession]:
    async with session_maker() as session:
        yield session
