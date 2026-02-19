from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env")

    API_KEY:str
    DB_USERNAME:str
    DB_PASSWORD:str

settings = Settings()
print(settings.API_KEY, settings.DB_USERNAME, settings.DB_PASSWORD )