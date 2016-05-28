import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

DEBUG = bool(os.environ.get('DEBUG', False))
if DEBUG:
    BASE_URL = 'http://localhost:8000/api'
else:
    BASE_URL = 'http://swapi.co/api'
