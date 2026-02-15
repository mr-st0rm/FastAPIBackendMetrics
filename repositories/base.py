import structlog

from sqlalchemy.ext.asyncio import AsyncSession


logger = structlog.get_logger()


class BaseRepository:
    def __init__(self, session: AsyncSession) -> None:
        self.session = session

    async def commit(self) -> None:
        try:
            await self.session.commit()
        except Exception as e:
            await self.session.rollback()
            logger.error("Error while commiting", error=e, exc_info=True)
