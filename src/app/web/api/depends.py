from fastapi import Depends
from redis.asyncio import Redis

from src.app.config import SETTINGS
from src.app.data.db import DataBase
from src.app.service.service import Service


def get_redis_client() -> Redis:
    return Redis(host=SETTINGS.redis_host)


def get_data_base(
        redis_client: Redis = Depends(get_redis_client)
) -> DataBase:
    return DataBase(client=redis_client)


def get_service(
        data_base: DataBase = Depends(get_data_base)
) -> Service:
    return Service(data_base)
