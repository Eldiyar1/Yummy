from .base import *
from .development import *

CORS_ALLOWED_ORIGINS = [
    "http://localhost:8080",
    "http://localhost:3080",
    "http://127.0.0.1:8001",
    "http://127.0.0.1:3000",
    "http://127.0.0.1:4040",
    "https://9151-46-251-214-255.ngrok-free.app",
]
ALLOWED_HOSTS = ["*"] + CORS_ALLOWED_ORIGINS
CORS_ALLOW_METHODS = [
    'GET',
    'POST',
    'PUT',
    'DELETE',
]

CORS_ALLOW_HEADERS = [
    'Content-Type',
]

CORS_ALLOW_CREDENTIALS = True
CSRF_TRUSTED_ORIGINS = ["https://9151-46-251-214-255.ngrok-free.app"]
CORS_ALLOW_ALL_ORIGINS = True

