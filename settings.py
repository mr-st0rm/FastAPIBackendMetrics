from pydantic_settings import BaseSettings, SettingsConfigDict


class DatabaseSettings(BaseSettings):
    DB_DRIVER: str = "asyncpg"
    DB_HOST: str
    DB_PORT: int
    DB_USER: str
    DB_PASSWORD: str
    ECHO: bool = False

    @property
    def db_url(self) -> str:
        return f"postgresql+{self.DB_DRIVER}://{self.DB_USER}:{self.DB_PASSWORD}@{self.DB_HOST}:{self.DB_PORT}"


class ApplicationSettings(DatabaseSettings):
    model_config = SettingsConfigDict(env_file=".env.base", extra="ignore")


def get_settings() -> ApplicationSettings:
    return ApplicationSettings()
