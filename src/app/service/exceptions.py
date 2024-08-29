"""Модуль, содержащий исключения для работы с данными в сервисе"""


class LexicomError(Exception):
    """ Базовый класс для исключений в сервисе"""

    pass


class RecordNotFoundError(LexicomError):
    """Исключение, выбрасываемое, когда запись не найдена."""

    pass


class RecordAlreadyExistsError(LexicomError):
    """Исключение, выбрасываемое, когда запись с данным ключом уже существует."""

    pass
