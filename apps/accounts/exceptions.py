from rest_framework import serializers,status
from rest_framework.exceptions import APIException


# Файл для хранения всех ошибок


# Ошибки бизнез логики
class EmailRequiredException(Exception):
    '''Email обязателен'''
    pass

class IncorrectCreateSuperUser(Exception):
    '''Неправильно создан админ'''
    pass

class UserAlreadyExists(Exception):
    ''' Такой пользователь уже есть '''
    pass

class OldPasswordIncorrect(serializers.ValidationError):
    default_detail = "Старый пароль неверный"

# ошибки HTTP
class UnauthorizedException(APIException):
    status_code = status.HTTP_401_UNAUTHORIZED
    default_detail = "Не авторизован"
    default_code = "unauthorized"


