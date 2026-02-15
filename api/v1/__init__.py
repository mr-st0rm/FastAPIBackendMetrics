from fastapi import APIRouter

from .messages import router as messages_router

api_v1_router = APIRouter(
    prefix="/api/v1",
)
api_v1_router.include_router(messages_router)
