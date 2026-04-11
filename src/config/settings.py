import os
from dotenv import load_dotenv

# Load .env file
load_dotenv()

class Settings:
    GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
    GEMINI_MODEL = os.getenv("GEMINI_MODEL")

    MISTRAL_API_KEY = os.getenv("MISTRAL_API_KEY")
    MISTRAL_MODEL = os.getenv("MISTRAL_MODEL")

settings = Settings()
