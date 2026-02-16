import structlog
from fastapi import APIRouter

router = APIRouter()
logger = structlog.get_logger()


@router.get("/health")
async def health() -> dict:
    logger.debug("Health check")
    return {"status": "healthy"}
