import os
from dotenv import load_dotenv

load_dotenv()

# API Configuration
API_BASE_URL = os.getenv('DATASCRIBE_API_BASE_URL', 'https://datascribe.cloud/data')
API_TOKEN = os.getenv('DATASCRIBE_API_TOKEN', '')

# Default request settings
DEFAULT_TIMEOUT = 30
DEFAULT_HEADERS = {
    'Content-Type': 'application/json',
    'Authorization': f'Bearer {API_TOKEN}'
}