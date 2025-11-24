import os
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("API_KEY")

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

PROMPT_PATH = os.path.join(BASE_DIR, "prompt.txt")
KB_PATH = os.path.join(BASE_DIR, "knowledgebase.txt")

MODEL_NAME = "gemini-2.5-pro"