from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from prometheus_client.asgi import make_asgi_app

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


prometheus_app = make_asgi_app()
app.mount("/metrics", prometheus_app)
