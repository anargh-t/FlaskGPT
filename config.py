import os
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env file

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'your_secret_key')
    OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
    DEEPSEEK_API_KEY = os.getenv('DEEPSEEK_API_KEY')
    GEMINI_API_KEY = os.getenv('GEMINI_API_KEY')
