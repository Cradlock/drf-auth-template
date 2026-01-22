from rest_framework import serializers,status
from rest_framework.exceptions import APIException





# Файл для хранения всех ошибок


# Ошибки бизнез логики
class EmailRequiredException(APIException):
    '''Email обязателен'''
    status_code = status.HTTP_400_BAD_REQUEST 
    default_detail = "email обязятелен"
    default_code = "email_required"

class IncorrectCreateSuperUser(Exception):
    '''Неправильно создан админ'''
    pass 

class UserAlreadyExists(APIException):
    ''' Такой пользователь уже есть '''
    status_code = status.HTTP_409_CONFLICT 
    default_detail = "Такой пользовталье уже есть"
    default_code = "user_already_exists"



class OldPasswordIncorrect(serializers.ValidationError):
    default_detail = "Старый пароль неверный"


# ошибки HTTP
class GoogleTokenError(APIException):
    ''' Ошибка google токенов '''
    status_code = status.HTTP_504_GATEWAY_TIMEOUT  
    default_detail = "Ошибка google токенов"
    default_code = "google_token_error"

class InvalidIdToken(APIException):
    """Когда id_token недействителен или не содержит email"""
    status_code = status.HTTP_400_BAD_REQUEST 
    default_detail = "id token недейстителен"
    default_code = "invalid_id_token"

class MissingIdToken(APIException):
    '''Пропущен id_token'''
    status_code = status.HTTP_403_FORBIDDEN
    default_detail = "Не отправлен id_token"
    default_code = "missing_id_token"

class UnauthorizedException(APIException):
    status_code = status.HTTP_401_UNAUTHORIZED
    default_detail = "Не авторизован"
    default_code = "unauthorized"

class TokenExpiredException(APIException):
    status_code = status.HTTP_401_UNAUTHORIZED
    default_detail = "Токен истёк"
    default_code = "token_expired"


class DontSendRedirectUri(APIException):
    status_code = status.HTTP_400_BAD_REQUEST 
    default_detail = "Не отправлен redirect_uri"
    default_code = "not_redirect_uri"

class MissingCodeOrRedirectUri(APIException):
    status_code = status.HTTP_400_BAD_REQUEST
    default_detail = "Не передан 'code' или 'redirect_uri'"
    default_code = "missing_code_or_redirect_uri"

class MissingUidbOrToken(APIException):
    status_code = status.HTTP_400_BAD_REQUEST 
    default_detail = "Не передан 'token' или 'uidb64' "
    default_code = "missing_token_uidb64"

class UserNotFound(APIException):
    status_code = status.HTTP_404_NOT_FOUND 
    default_detail = "Пользователь не найден"
    default_code = "user_not_found"





