from fastapi import APIRouter, Depends

from api.deps import get_messages_service
from services.messages import MessagesService

router = APIRouter()


@router.get("/message/{message_id}")
async def get_message(
    message_id: int,
    service: MessagesService = Depends(get_messages_service),
) -> str:
    return await service.get_message_text(message_id)
