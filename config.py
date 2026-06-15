from pydantic_settings import BaseSettings, SettingsConfigDict


class Config(BaseSettings):
    host: str = "localhost"
    port: int = 3306
    user: str = "root"
    password: str | None = None
    database: str | None = None
    use_pure: bool = True

    model_config = SettingsConfigDict(env_file="config.env", env_prefix="DB_")
