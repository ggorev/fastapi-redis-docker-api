from typing import Literal

from pydantic import computed_field
from pydantic_settings import (
    BaseSettings,
    SettingsConfigDict,
)


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file="docker/.env"
    )
    ENVIRONMENT: Literal["DEV", "PROD"] = "DEV"

    @computed_field  # type: ignore[prop-decorator]
    @property
    def redis_host(
            self
    ) -> str:
        return "localhost" if self.ENVIRONMENT == "DEV" else "redis"


SETTINGS = Settings()
