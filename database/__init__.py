from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine

from settings import get_settings

settings = get_settings()

engine = create_async_engine(
    settings.db_url,
    echo=settings.ECHO,
    connect_args={"server_settings": {"application_name": "METRICS_SERVICE"}},
)
session_maker = async_sessionmaker(engine, expire_on_commit=False)
