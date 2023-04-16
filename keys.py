import os
from dotenv import load_dotenv

load_dotenv()

base_url = os.getenv("BASE_URL")
api_key_id = os.getenv("API_KEY_ID")
api_secret = os.getenv("API_SECRET")