import os
from dotenv import load_dotenv, find_dotenv
from django.core.management.utils import get_random_secret_key

dotenv_file = find_dotenv()
load_dotenv(dotenv_file, override=True)

SECRET_KEY = os.getenv('SECRET_KEY', get_random_secret_key())
DB_ENGINE = os.getenv('DB_ENGINE', '')
DB_HOST = os.getenv('DB_HOST', '')
DB_PORT = os.getenv('DB_PORT', '')
DB_NAME = os.getenv('DB_NAME', '')
DB_USER = os.getenv('DB_USER', '')
DB_PASSWORD = os.getenv('DB_PASSWORD', '')
