from sqlalchemy.orm import Mapped, mapped_column

from database.models.base import CreatedAndUpdatedAtBaseModel


class Message(CreatedAndUpdatedAtBaseModel):
    """
    Attributes:
        id: Идентификатор сообщения
        text: Тело сообщение
    """

    __tablename__ = "message"

    id: Mapped[int] = mapped_column(primary_key=True)
    text: Mapped[str]
