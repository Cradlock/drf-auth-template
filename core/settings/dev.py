# Настройки для разработки 
from .base import *

# Флаг для разработки
DEBUG = True

# Доступные хосты
ALLOWED_HOSTS = ["*"]

# Настройка паролей
AUTH_PASSWORD_VALIDATORS = []


# Настройка celery
CELERY_BROKER_URL = f"redis://{REDIS_HOST}:{REDIS_PORT}/{REDIS_DB_BROKER}"
CELERY_RESULT_BACKEND = f"redis://{REDIS_HOST}:{REDIS_PORT}/{REDIS_DB_BACKEND}"

CELERY_ACCEPT_CONTENT = ['json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'



# настройка кеша через редис
CACHES["default"]["LOCATION"] = f"redis://{REDIS_HOST}:{REDIS_PORT}/{REDIS_DB_CACHE}"



# настройка cors
CORS_ALLOWED_ORIGINS = [
    "http://localhost:3000","http://127.0.0.1:3000"
]

# настройка cookie

SESSION_COOKIE_SECURE = False

CSRF_COOKIE_SECURE = False

SESSION_COOKIE_SAMESITE = 'Strict'

CSRF_COOKIE_SAMESITE = 'Strict'





REFRESH_TOKEN_PARAMETERS = {
    "httponly":True,
    "secure":False,
    "samesite":"Strict"
}







