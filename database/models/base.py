import datetime

from sqlalchemy import DateTime, func
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class BaseModel(DeclarativeBase):
    __abstract__ = True


class CreatedAndUpdatedAtBaseModel(BaseModel):
    __abstract__ = True

    created_at: Mapped[datetime.datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now()
    )
    updated_at: Mapped[datetime.datetime | None] = mapped_column(
        DateTime(timezone=True),
        server_onupdate=func.now(),
    )
