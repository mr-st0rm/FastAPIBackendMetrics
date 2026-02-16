import asyncio
from typing import Literal


class ProcessService:
    async def process_data(
        self, payload: dict[Literal["data"], str]
    ) -> dict[Literal["data"], str]:
        timeout = 0.5
        if payload["data"] == "bottleneck":
            timeout = 2

        await asyncio.sleep(timeout)

        return payload
