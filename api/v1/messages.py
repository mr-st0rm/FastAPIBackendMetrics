from fastapi import APIRouter

router = APIRouter()


@router.get("/message/{message_id}")
async def get_message(message_id: int):
    ...
