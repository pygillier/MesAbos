from pydantic_settings import BaseSettings
import os


class Settings(BaseSettings):
    app_name: str = os.getenv("APP_NAME", "MesAbos")
    api_prefix: str = os.getenv("API_PREFIX", "")

    database_url: str = os.getenv(
        "DATABASE_URL",
        "mysql+pymysql://mesabos_usr:mesabos_pwd@localhost:3306/mesabos?charset=utf8mb4",
    )


settings = Settings()
