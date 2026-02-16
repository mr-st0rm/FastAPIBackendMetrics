FROM python:3.12-slim as builder

WORKDIR /app
RUN pip install poetry==2.3.2 && poetry self add poetry-plugin-export
COPY pyproject.toml poetry.lock ./
RUN poetry config virtualenvs.create false \
    && poetry install --no-interaction --no-ansi --no-root \
    && pip check

FROM python:3.12-slim

RUN addgroup --system app && adduser --system --ingroup app app
WORKDIR /app

COPY --from=builder /usr/local /usr/local
COPY . .

USER app

EXPOSE 8080
