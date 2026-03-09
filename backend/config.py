import os
from dotenv import load_dotenv



load_dotenv()

FACEIT_API_KEY = os.getenv("FACEIT_API_KEY")

if not FACEIT_API_KEY:
    raise RuntimeError("FACEIT_API_KEY is not set")
