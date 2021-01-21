import os
from dotenv import load_dotenv, find_dotenv

from pathlib import Path  # Python 3.6+ only
env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)

ACCESS_TOKEN = os.environ.get("ACCESS_TOKEN")
SECRET_ACCESS_TOKEN = os.environ.get("SECRET_ACCESS_TOKEN")
API_KEY = os.environ.get("API_KEY")
SECRET_API_KEY = os.environ.get("SECRET_API_KEY")
PHOTO_LOCATION = os.environ.get("PHOTO_LOCATION")