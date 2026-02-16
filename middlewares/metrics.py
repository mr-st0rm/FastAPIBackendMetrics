import time

from prometheus_client import Counter, Histogram
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.requests import Request

REQUESTS_TOTAL = Counter(
    "http_requests_total", "Total HTTP requests", ["method", "path", "status"]
)

REQUEST_LATENCY = Histogram(
    "http_request_duration_seconds",
    "HTTP request latency",
    ["method", "path"],
    buckets=(0.1, 0.2, 0.3, 0.5, 0.7, 1, 1.5, 2, 3),
)


class MetricsMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        start_time = time.perf_counter()
        response = await call_next(request)
        duration = time.perf_counter() - start_time

        path = request.url.path

        REQUESTS_TOTAL.labels(
            method=request.method, path=path, status=response.status_code
        ).inc()

        REQUEST_LATENCY.labels(method=request.method, path=path).observe(duration)

        return response
