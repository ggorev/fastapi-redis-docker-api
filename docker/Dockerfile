FROM python:3.11.2-slim-bullseye AS builder

WORKDIR /app

COPY pyproject.toml pdm.lock ./

RUN --mount=type=cache,target=/root/.cache \
    pip install --no-cache-dir pdm==2.15 \
    && pdm install --prod --no-editable && pdm cache clear

FROM python:3.11.2-slim-bullseye AS final

ENV PYTHONUNBUFFERED=1
ENV PYTHONPATH=/app
ENV PATH="/app/.venv/bin:$PATH"


WORKDIR /app

COPY --from=builder /app /app
COPY src/ ./src
