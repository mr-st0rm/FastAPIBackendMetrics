import asyncio

import structlog

from api.v1.schemas.process import ProcessRequest

logger = structlog.get_logger()


class ProcessService:
    async def process_data(self, payload: ProcessRequest) -> ProcessRequest:
        timeout = 0.5
        if payload.data == "bottleneck":
            timeout = 2

        await asyncio.sleep(timeout)

        logger.info(
            f"Processed {payload.data} with timeout {timeout}s",
            payload=payload.model_dump_json(),
            timeout=timeout,
        )

        return payload
