from dotenv import load_dotenv
from pydantic import BaseSettings

class Settings(BaseSettings):
    database_uri: str

def load_settings():
    load_dotenv()
    settings = Settings()
    return settings