# Базовый шаблон django-rest-framework

<hr>
<p> 
 Шаблон чтобы я мог быстро начать работать с drf проектом 
 cо встроенной системой авторизации через `email`. Также добавленной
 ассинхроностью и веб-сервером `uvicorn`
</p>
<hr>

## Настроенные сервисы:
- SimpleJWT: авторизация через jwt (access: Bearer , refresh: httpOnly cookie)
- ASGI: асинхронная точка входа для Django
- Redis: кэширование, pub/sub, blacklist для токенов
- Celery: обработка фоновых задач
- Channels: WebSocket и real-time уведомления

## Зависимости проекта:
    - `django=6.0.1`: Фреймфорк для веб-сервера
    - `django-cors-headers=4.9.0`: Библиотека для настройки CORS политики
    - `djangorestframework=3.16.1`: Дополнение к `Django` добавляет возможность создать API
    - `djangorestframework-simplejwt=5.5.1`: Библиотека для работы с `JWT` токенам
    - `drf-yasg=1.21.11`: Работа со `swagger` авто-документация
    - `django-jazzmin=3.0.1`: Модифицированная админ-панель
    - `redis=7.1.0`: Быстрая база данных. Все хранится в RAM, поддерживает асинхронность. Нужен для кеширования
    - `channels_redis=4.3.0`: Backend для channels через redis
    - `channels=4.3.2`: Библиотека для веб-сокетов
    - `uvicorn=0.40.0`: Асинхронный веб сервер на python
    - `aioredis=2.0.1`: Библиотека для асихронных операций в redis
    - `psycopg2-binary=2.9.11`: Библиотека для работы с PostgreSQL
    - `dotenv=0.9.9`: Библиотека для работы с `.env` переменными
    - `httpx=0.28.1`: Библиотека для ассинхроной работы с http
    - `celery=5.6.2`: Библиотека для фоновых задач 

## Cтруктура проекта:
<pre>
<code>
apps/
    accounts/   <--- приложение аутентификации
        services/ <--- Сервисный слой
            __init__.py 
            account.py <--- Работа с аккаунтами
            social_google.py <--- Работа с google 
            token.py <--- Работа с токенами
        templates/ <--- html страницы
            email/
                confirm.html 
        views/ <--- `views` 
            __init__.py 
            auth_views.py <--- Аутентификация 
            social_views.py <--- Социальные views 
            user_views.py <--- Действие с аккаунтом
        
        __init__.py 
        admins.py <--- Админ панель
        apps.py <--- Конфигуратор приложения
        exceptions.py <--- Набор исключений
        managers.py <--- Менеджер для Account 
        models.py <--- Модели
        permissions.py <--- Разрешения
        selectors.py <--- Селекторы для получения данных из бд
        serializers.py <--- Сериализаторы 
        tests.py <--- Тесты 
        urls.py <--- Маршруты

    base/       <--- Базовое приложение 
        management/
            commands/
               __init__.py 
               runserver_asgi.py <--- Кастомная команда для запуска асинхронного сервера 
            __init__.py 
        
        utils/ <--- Модуль для переиспользуемых команд
            __init__.py
            datetime.py 
            email.py 
            strings.py 
            validators.py 

        __init__.py 
        apps.py 
        mixins.py <--- Переиспользуемые миксины 
        urls.py <--- Общий маршрутизатор всех приложений

core/       <--- Основной модуль проекта
    settings/   <--- Настройка
        base.py <--- Базовые настройки
        dev.py  <--- Настройки для разработки
        prod.py <--- Настройки для продакшена
    __init__.py 
    asgi.py <--- Асинхронный сервер
    celery.py <--- Файл для настройки фоновых задач
    urls.py <--- Роутер маршрутов
    wsgi.py <--- Синхронный сервер


.gitignore
Dockerfile 
manage.py 
README.md 
requirements.txt


</code>
</pre>
        



## Некоторые добавленные функции:
- `python manage.py runserver_asgi`: Запуск для асинхронного дебагга

