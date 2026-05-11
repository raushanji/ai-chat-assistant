from dotenv import load_dotenv
import os

load_dotenv()

class Settings:
    APP_NAME = os.getenv("APP_NAME")
    ENVIRONMENT = os.getenv("ENVIRONMENT")
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

settings = Settings()