from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_metrics_endpoint():
    response = client.get("/metrics")
    assert response.status_code == 200
    body = response.text
    # Проверяем, что основные метрики присутствуют
    assert "http_requests_total" in body
    assert "http_request_duration_seconds_bucket" in body
