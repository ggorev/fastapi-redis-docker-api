"""
Модуль, предоставляющий простой интерфейс для работы с базой данных Redis с использованием асинхронного клиента Redis.
"""

from typing import Optional

from redis.asyncio import Redis
from redis.typing import (
    EncodableT,
    KeyT,
    ResponseT,
)


class DataBase:
    """Класс для взаимодействия с базой данных Redis."""

    def __init__(
            self,
            client: Redis
    ):
        """
        Инициализация класса DataBase с клиентом Redis.

        :param client: Экземпляр Redis.
        :type client: redis.asyncio.client.Redis

        :return: None
        :rtype: NoneType
        """

        self.client = client

    async def get(
            self,
            key: KeyT
    ) -> Optional[ResponseT]:
        """
        Получение значения, связанного с заданным ключом, из базы данных Redis.

        :param key: Ключ для получения значения.
        :type key: redis.typing.KeyT

        :return: Значение, связанное с ключом, или None, если ключ не существует.
        :rtype: typing.Optional[redis.typing.ResponseT]
        """

        return await self.client.get(key)

    async def add(
            self,
            key: KeyT,
            value: EncodableT
    ) -> Optional[ResponseT]:
        """
        Добавление новой пары ключ-значение в базу данных Redis, если ключ ещё не существует.

        :param key: Ключ для установки.
        :type key: redis.typing.KeyT
        :param value: Значение, связанное с ключом.
        :type value: redis.typing.EncodableT

        :return: Значение, связанное с ключом, если ключ был успешно добавлен,
                                  или None, если ключ уже существует.
        :rtype: typing.Optional[redis.typing.ResponseT]
        """

        return await self.client.get(key) if await self.client.set(key, value, nx=True) else None

    async def update(
            self,
            key: KeyT,
            value: EncodableT
    ) -> Optional[ResponseT]:
        """
        Обновление значения, связанного с заданным ключом, в базе данных Redis, если ключ уже существует.

        :param key: Ключ для обновления.
        :type key: redis.typing.KeyT
        :param value: Новое значение, связанное с ключом.
        :type value: redis.typing.EncodableT

        :return: Новое значение, связанное с ключом, если ключ был успешно обновлён,
                                  или None, если ключ не существовал.
        :rtype: typing.Optional[redis.typing.ResponseT]
        """

        return await self.client.get(key) if await self.client.set(key, value, xx=True) else None
