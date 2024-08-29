from fastapi import (
    APIRouter,
    Depends,
    Query,
)
from starlette import status

from src.app.service.service import Service
from src.app.web.api.depends import get_service
from src.app.web.api.schemas import DataScheme

router = APIRouter(
    prefix='/data',
    tags=['Данные']
)


@router.get('')
async def check_data(
        phone: str = Query(..., description='Номер телефона для получения адреса.'),
        service: Service = Depends(get_service)
) -> DataScheme:
    """Получение данных."""

    result = await service.get(
        key=phone,
    )
    return DataScheme(
        phone=phone,
        address=result
    )


@router.post(
    '',
    status_code=status.HTTP_201_CREATED
)
async def write_data(
        data: DataScheme,
        service: Service = Depends(get_service)
) -> DataScheme:
    """Запись данных."""

    result = await service.add(
        key=data.phone,
        value=data.address
    )
    return DataScheme(
        phone=data.phone,
        address=result
    )


@router.put('')
async def update_data(
        data: DataScheme,
        service: Service = Depends(get_service)
) -> DataScheme:
    """Обновление данных."""

    result = await service.update(
        key=data.phone,
        value=data.address
    )
    return DataScheme(
        phone=data.phone,
        address=result
    )
