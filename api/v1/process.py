from typing import Literal

from fastapi import APIRouter, Depends

from services.process import ProcessService

router = APIRouter()


@router.post("/process")
async def process_data(
    data: dict[Literal["data"], str],
    service: ProcessService = Depends(),
) -> dict[Literal["data"], str]:
    return await service.process_data(data)
