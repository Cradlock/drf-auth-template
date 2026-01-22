import os

from pathlib import Path
from dotenv import load_dotenv
from datetime import timedelta

# Базовый путь 
BASE_DIR = Path(__file__).resolve().parent.parent.parent


# Загрузка секретных данных
load_dotenv(BASE_DIR / ".env")



# Загрузка секретных переменных

# Cекретный ключ 
SECRET_KEY = os.getenv("SECRET_KEY")

# Настройки редиса
REDIS_HOST = os.getenv("REDIS_HOST", "localhost")
REDIS_PORT = os.getenv("REDIS_PORT", 6379 )
REDIS_PASSWORD = os.getenv("REDIS_PASSWORD", None)

REDIS_DB_BACKEND = 0
REDIS_DB_BROKER = 1
REDIS_DB_CACHE = 2

# Настройка email 
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = os.getenv("EMAIL_HOST",587)
EMAIL_USE_TLS = os.getenv("EMAIL_USE_TLS",True)
EMAIL_HOST_USER = os.getenv("EMAIL_HOST_USER")
EMAIL_HOST_PASSWORD = os.getenv("EMAIL_HOST_PASSWORD")
DEFAULT_FROM_EMAIL = os.getenv("DEFAULT_FROM_EMAIL")


# Настройки базы данных
DB_HOST = os.getenv("DB_HOST","localhost")
DB_NAME = os.getenv("DB_NAME","project")
DB_PORT = os.getenv("DB_PORT","5432")
DB_PASSWORD = os.getenv("DB_PASSWORD","password")
DB_USER = os.getenv("DB_USER","myuser")


# Установленные приложения
INSTALLED_APPS = [
    # Стандартные приложения django
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Документация
    'drf_yasg',

    # Модификация админ-панели
    'jazzmin',

    # Для создания API
    'rest_framework',
    'rest_framework.authtoken',
    
    # Приложение для JWT
    'rest_framework_simplejwt',

    # Для blacklist в simpleJWT
    'rest_framework_simplejwt.token_blacklist',

    # Для настройки CORS политики
    'corsheaders',

    # Для веб сокетов
    'channels',
    
    # Фоновые задачи
    'django_celery_beat',

    # мои приложени
    'apps.base', # Дополнительные функции которые используются во всех приложениях
    'apps.accounts', # базовая авторизация (можно улучшать)
]


# Cлои между клиентом и сервером 
MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# Центральный маршрутизатор
ROOT_URLCONF = 'core.urls'


# Дефолтное primary key
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Работа с html шаблонами
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR,'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# База данных

#DATABASES = {
#    "default":{
#        "ENGINE": "django.db.backends.postgresql",
#        "NAME": DB_NAME,
#        "USER": DB_USER,
#        "PASSWORD": DB_PASSWORD,
#        "HOST": DB_HOST,
#        "PORT": DB_PORT
#    }
#}

# Если нету postgresql
DATABASES = {
   "default":{
       'ENGINE': 'django.db.backends.sqlite3',
       'NAME': BASE_DIR / 'db.sqlite3', 
   }
}



# Файл для указания синхронного веб-сервера
WSGI_APPLICATION = 'core.wsgi.application'

# Файл для указания асинхронного веб-сервера
ASGI_APPLICATION = 'core.asgi.application'

# Кастомная модель :пользователя
AUTH_USER_MODEL = "accounts.Account"

# Настройки языка
LANGUAGE_CODE = 'ru-ru'

# Часовой пояс
TIME_ZONE = 'UTC'

# Будет ли использовать перевод?
USE_I18N = True

# Нужен для работы с часовми поясами
USE_TZ = True

# Фоновые задачи 
CELERY_ENABLE_UTC = True

# Настройка статических файлов
STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'

# Настройка медиа файлов
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'





# Настройка django-rest_framework
REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES":(
        "rest_framework_simplejwt.authentication.JWTAuthentication",
    ),
    "DEFAULT_PERMISSION_CLASSES": (
        "rest_framework.permissions.IsAuthenticated",
    )
}





# Настройка Redis Cache
CACHES = {
    "default":{
        "BACKEND": "django_redis.cache.RedisCache",
        # "LOCATION": ... <- указано в dev|prod
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
            "COMPRESSOR": "django_redis.compressors.zlib.ZlibCompressor",
            "IGNORE_EXCEPTIONS": True
        },
        "TIMEOUT": 200
    }
}


# Настройка сors
CORS_ALLOW_CREDENTIALS = True 

CORS_ALLOW_HEADERS = [
    'authorization',
    'content-type',
    'accept'
]

CORS_ALLOW_METHODS = [
    'GET','POST',
    'PUT','PATCH',
    'DELETE','OPTIONS'
]



# Настройка simpleJWT
SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME":  timedelta(minutes=20),
    "REFRESH_TOKEN_LIFETIME": timedelta(days=7),

    "ROTATE_REFRESH_TOKENS": True, # обновление refresh при использовании
    "BLACKLIST_AFTER_ROTATION": True, # отправлять старый в black list
    
    "ALGORITHM":"HS256",
    "SIGNING_KEY": SECRET_KEY,

    "AUTH_HEADER_TYPES":("Bearer",),
    "AUTH_TOKEN_CLASSES": ("rest_framework_simplejwt.tokens.AccessToken"),
    
    "TOKEN_USER_CLASS": "rest_framework_simplejwt.models.TokenUser"
}






# Настройка swagger
SWAGGER_SETTINGS = {
    'SECURITY_DEFINITIONS':{
        "BEARER":{
            'type':'apiKey',
            'name': 'Authorization',
            'in': 'header',
            'description': 'Шаблон для работы с jwt '
        }
    },
    'USE_SESSION_AUTH': False,
}













