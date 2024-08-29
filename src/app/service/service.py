"""
Модуль, предоставляющий сервис для работы с данными в базе данных Redis.
"""

from redis.typing import (
    EncodableT,
    KeyT,
    ResponseT,
)

from src.app.data.db import DataBase
from src.app.service.exceptions import (
    RecordAlreadyExistsError,
    RecordNotFoundError,
)


class Service:
    """Сервис для работы с данными в базе данных Redis."""

    def __init__(
            self,
            db: DataBase
    ):
        """
        Инициализация класса Service с экземпляром DataBase.

        :param db:
        :type db:

        :return: None
        :rtype: NoneType
        """

        self.db = db

    async def get(
            self,
            key: KeyT
    ) -> ResponseT:
        """
        Получение данных по ключу из базы данных.

        :param key: Ключ для получения данных.
        :type key: redis.typing.KeyT

        :return: Значение, связанное с ключом, или None, если ключ не найден.
        :rtype: redis.typing.ResponseT

        :raises src.app.service.exceptions.RecordNotFoundError: Если запись с данным ключом не найдена.
        """

        value = await self.db.get(key=key)
        if value is not None:
            return value
        raise RecordNotFoundError(f'Не найдено записи с ключом: {key!r}')

    async def add(
            self,
            key: KeyT,
            value: EncodableT
    ) -> ResponseT:
        """
        Добавление новой записи в базу данных.

        :param key: Ключ для записи.
        :type key: redis.typing.KeyT
        :param value: Значение, связанное с ключом.
        :type value: redis.typing.EncodableT

        :return: Значение, связанное с ключом, если запись была успешно добавлена.
        :rtype: redis.typing.ResponseT

        :raises src.app.service.exceptions.RecordAlreadyExistsError: Если запись с данным ключом уже существует
        """
        record = await self.db.add(
            key=key,
            value=value
        )
        if record is not None:
            return record
        raise RecordAlreadyExistsError(f'Данные с ключом {key!r} уже записаны')

    async def update(
            self,
            key: KeyT,
            value: EncodableT
    ) -> ResponseT:
        """
        Обновление записи в базе данных.

        :param key: Ключ для обновления записи.
        :type key: redis.typing.KeyT
        :param value: Новое значение для записи.
        :type value: redis.typing.EncodableT

        :return: Обновлённое значение, связанное с ключом.
        :rtype: redis.typing.ResponseT

        :raises src.app.service.exceptions.RecordNotFoundError: Если запись с данным ключом не найдена.
        """

        record = await self.db.update(
            key=key,
            value=value
        )
        if record is not None:
            return record
        raise RecordNotFoundError(f'Не найдено записи с ключом: {key!r}')
