Цель задания: 
- Проверить навыки создания backend-сервиса с observability (метрики, логи), интеграцией Prometheus/Node Exporter и визуализацией в Grafana. 

- Результат — GitHub-репозиторий с историей коммитов (минимум 3–5, чтобы избежать подозрений на ИИ), README.md (инструкции по запуску, объяснение решений, trade-off'ы) и Docker Compose для локального тестирования.

Требования:
* Python 3.10+.
* FastAPI для API.
* SQLAlchemy с PostgreSQL (для простоты, храните mock-данные или логи, если нужно).
* Prometheus для сбора метрик
* Node Exporter для системных метрик (CPU, memory в контейнере).
* Grafana для дашбордов (provisioning с JSON-файлами).
* Structured logging (JSON с logging или structlog).
* Docker и Docker Compose.
* Pytest для тестов.
* Читаемый код с type hints, docstrings, обработкой ошибок и базовой безопасностью (OWASP: валидация input).


Задача:

    FastAPI-приложение:
        Создайте простое приложение со следующими эндпоинтами:
            GET /health: Возвращает {"status": "healthy"}.
            GET /message/{id}: Возвращает статическое сообщение (например, из mock-БД в PostgreSQL: таблица messages с id, text).
            POST /process: Принимает JSON ({"data": str}), симулирует обработку (sleep ~0.5s для latency) и возвращает echo.
            GET /metrics: Экспорт Prometheus-метрик (автоматически через instrumentator).

    Добавьте кастомные метрики: Счетчик запросов по эндпоинтам (Counter), гистограмма latency (Histogram).
    Логи: Структурированные JSON-логи.

    Observability:
        Интегрируйте Prometheus: Собирайте метрики приложения (requests total, latency, errors) и системные от Node Exporter (CPU, mem, disk).
        Логи: Настройте сбор логов (Alloy/Promtail) и отправку их в Loki.
        Grafana: Создайте дашборд (JSON-export в репо) с панелями: Графики запросов/sec, latency percentile, CPU/mem usage, логи приложения, counter для errors/warnings.

    Заполнение данными:
        Mock-данные в PostgreSQL: ≥10 сообщений (seed-скрипт при старте).

    Оптимизация и анализ:
        Симулируйте bottleneck (медленный запрос), опишите в README, как выявить (через Grafana queries).

    Добавьте алерт-rule в Prometheus (например, high latency >1s).

    Контейнеризация:
        Безопасный Dockerfile для приложения.

    Docker Compose со всеми необходимыми сервисами.

    Тестирование:
        Pytest: Unit для эндпоинтов, интеграционные для метрик (проверьте /metrics response).

    Документация:
        Напишите README.md:
            Инструкция по запуску приложения локально через Docker Compose
            Объяснение метрик/логов
            Добавьте файл JSON-export из созданной вами дашбордой в репозиторий

    GitHub:
        Код должен быть выложен на GitHub. Проекты с одним коммитом рассматриваться не будут.