from pydantic_settings import BaseSettings, SettingsConfigDict


class DatabaseSettings(BaseSettings):
    POSTGRES_DRIVER: str = "asyncpg"
    POSTGRES_HOST: str
    POSTGRES_PORT: int
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    ECHO: bool = False

    @property
    def db_url(self) -> str:
        return f"postgresql+{self.POSTGRES_DRIVER}://{self.POSTGRES_USER}:{self.POSTGRES_PASSWORD}@{self.POSTGRES_HOST}:{self.POSTGRES_PORT}"


class ApplicationSettings(DatabaseSettings):
    model_config = SettingsConfigDict(env_file=".env.base", extra="ignore")


def get_settings() -> ApplicationSettings:
    return ApplicationSettings()
