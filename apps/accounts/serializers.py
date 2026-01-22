# Файл в котором указывается сериализаторы для работы с пользователями

from rest_framework import serializers
from django.contrib.auth import get_user_model

from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from apps.accounts.services import create_user,update_user_password,update_user_name 

User = get_user_model()


# Cериализатор для работы с токенами
class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token["email"] = user.email
        
        return token
    

# Cериализатор для пользователя

class RegisterUserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    frontend_url = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = (
            'email',
            'password',
            'first_name',
            'last_name',
            'frontend_url'
        )
    

class GetUserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = User
        fields = ('first_name', 'last_name' , 'id' , 'email' )



class RenameUserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = User
        fields = ( 'first_name' , 'last_name')



class ChangePasswordSerializer(serializers.Serializer):
    old_password = serializers.CharField(write_only=True)
    new_password = serializers.CharField(write_only=True)



