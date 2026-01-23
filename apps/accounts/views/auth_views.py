
from rest_framework.views import APIView 

from rest_framework.response import Response 
from rest_framework.permissions import IsAuthenticated,AllowAny 

from django.conf import settings 
from django.utils.http import urlsafe_base64_decode 
from django.contrib.auth.tokens import default_token_generator 
from django.contrib.auth import authenticate

from rest_framework_simplejwt.tokens import RefreshToken 
from rest_framework_simplejwt.exceptions import TokenError 


from rest_framework import status 


from apps.accounts.exceptions import (
    UnauthorizedException,
    TokenExpiredException,
    MissingUidbOrToken 
)

from apps.accounts.services import activate_user,issue_jwt_tokens 
from apps.accounts.selectors import get_user_by_id



# Логин
class LoginAPIView(APIView):
    permission_classes = [AllowAny,]
    def post(self, request, *args, **kwargs):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = authenticate(
            request,
            email=serializer.validated_data["email"],
            password=serializer.validated_data["password"]
        )

        if not user:
            raise UnauthorizedException()

        response = Response()
        return issue_jwt_tokens(user, response)


# Получение access токена
class RefreshAPIView(APIView):
    permission_classes = [AllowAny,]

    def post(self,request, *args,**kwargs):
        refresh_token = request.COOKIES.get("refresh")
        
        if not refresh_token:
            raise UnauthorizedException()

        try:
            refresh = RefreshToken(refresh_token)
            access_token = str(refresh.access_token) 
            
            return Response({"access":access_token},status=status.HTTP_200_OK)
        except TokenError:
            raise TokenExpiredException()



# Выход из аккаунта
class LogoutAPIView(APIView):
    permission_classes = [IsAuthenticated,]

    def post(self,request, *args, **kwargs):
        refresh_token = request.COOKIES.get("refresh")

        if refresh_token:
            try:
                token = RefreshToken(refresh_token)
                token.blacklist()
            except Exception:
                pass 

        response = Response(
            {"detail":"Вы вышли"},
            status=status.HTTP_200_OK
        )

        response.delete_cookie("refresh")

        return response 





# активация аккаунта
class ActivateAccountAPIView(APIView):
    
    def get(self,request,*args,**kwargs):
        uidb64 = kwargs.get("uidb64")
        token = kwargs.get("token")
        
        if not uidb64  or not token:
            raise MissingUidbOrToken()
        
        try:
            uid = urlsafe_base64_decode(uidb64).decode()
        except Exception:
            raise MissingUidbOrToken()

        user = get_user_by_id(uid) 
        
        if not default_token_generator.check_token(user,token):
            raise TokenExpiredException()

        activate_user(user)

        return Response({"detail":"ok"},status=status.HTTP_200_OK)











