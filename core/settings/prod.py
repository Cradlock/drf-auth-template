from .base import *

# Флаг разработки
DEBUG = False


# Доступные хосты
ALLOWED_HOSTS = [

]

# Проверка на пароли
AUTH_PASSWORD_VALIDATORS = [
    {
        # Проверяет, чтобы пароль не был слишком простым и не совпадал с личными данными пользователя
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        # Проверяет минимальную длину пароля
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
        'OPTIONS': {
            'min_length': 8,  # минимальная длина пароля
        }
    },
    {
        # Проверяет пароль на "сложность" — не только буквы, но и цифры и символы
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        # Проверяет, чтобы пароль не был слишком распространённым (например, 123456, qwerty)
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# настройка celery
REDIS_BASE = f"redis://{REDIS_PASSWORD}@{REDIS_HOST}:{REDIS_PORT}/"

CELERY_BROKER_URL = f"{REDIS_BASE}{REDIS_DB_BROKER}"
CELERY_RESULT_BACKEND = f"{REDIS_BASE}{REDIS_DB_BACKEND}"


CELERY_ACCEPT_CONTENT = ['json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'



# Настрока кеша через редис
CACHES["default"]["LOCATION"] = f"{REDIS_BASE}{REDIS_DB_CACHE}"


# Настройка cors
CORS_ALLOWED_ORIGINS = [

]

# Настройка cookie

SESSION_COOKIE_SECURE = True

CSRF_COOKIE_SECURE = True

SESSION_COOKIE_SAMESITE = 'None'

CSRF_COOKIE_SAMESITE = 'None'











