import logging
import sys

import structlog

from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from prometheus_client.asgi import make_asgi_app

from api.v1 import api_v1_router

logging.basicConfig(
    level=logging.INFO,
    stream=sys.stdout,
    format="%(asctime)s %(levelname)s %(name)s %(message)s",
)

structlog.configure(
    processors=[
        structlog.processors.JSONRenderer(),
        structlog.processors.TimeStamper(fmt="iso"),
        structlog.processors.add_log_level,
    ],
    logger_factory=structlog.stdlib.LoggerFactory(),
)

app = FastAPI(
    title="Metrics Application",
)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(api_v1_router)


prometheus_app = make_asgi_app()
app.mount("/metrics", prometheus_app)
