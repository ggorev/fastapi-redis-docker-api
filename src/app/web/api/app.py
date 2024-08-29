"""Модуль, содержащий настройки FastAPI и обработчики исключений для приложения."""

from fastapi import FastAPI
from starlette import status
from starlette.requests import Request
from starlette.responses import JSONResponse

from src.app.service.exceptions import (
    RecordAlreadyExistsError,
    RecordNotFoundError,
)
from src.app.web.api.router import router

app = FastAPI()
app.include_router(router)


@app.exception_handler(RecordNotFoundError)
async def record_not_found_handler(
        request: Request,
        exc: RecordNotFoundError
) -> JSONResponse:
    return JSONResponse(
        status_code=status.HTTP_404_NOT_FOUND,
        content={"message": str(exc)},
    )


@app.exception_handler(RecordAlreadyExistsError)
async def record_already_exists_handler(
        request: Request,
        exc: RecordAlreadyExistsError
) -> JSONResponse:
    return JSONResponse(
        status_code=status.HTTP_409_CONFLICT,
        content={"message": str(exc)},
    )
