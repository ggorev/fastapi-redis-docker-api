from pydantic import (
    BaseModel,
    Field,
)


class DataScheme(BaseModel):
    phone: str = Field(description='Номер телефона.')
    address: str = Field(description='Адрес.')
