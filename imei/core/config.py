import os

from dataclasses import dataclass

@dataclass
class Config:
    API_KEY_TG: str = os.getenv('API_KEY_TG')
    DATABASE_URL: str = (
        f"postgresql+asyncpg://"
        f"{os.getenv('POSTGRES_USER')}:{os.getenv('POSTGRES_PASSWORD')}"
        f"@database:5432/"
        f"{os.getenv('POSTGRES_DB')}"
    )
    DEBUG: bool = True
    PATH_LOG: str = os.path.normpath(os.path.join(os.getcwd(), "../logs"))


config = Config()

 
    


