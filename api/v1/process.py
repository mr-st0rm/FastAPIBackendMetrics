from fastapi import APIRouter, Depends

from api.v1.schemas.process import ProcessRequest
from services.process import ProcessService

router = APIRouter()


@router.post("/process")
async def process_data(
    data: ProcessRequest,
    service: ProcessService = Depends(),
) -> ProcessRequest:
    return await service.process_data(data)
