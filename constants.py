from dotenv import load_dotenv
import os

load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

SERVER_URL = "http://localhost"
PORT = 8000
ENV = "dev"
