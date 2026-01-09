# Файл в котором указывается сериализаторы для работы с пользователями

from rest_framework import serializers
from django.contrib.auth import get_user_model

from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from apps.accounts.services.register import create_user
from apps.accounts.services.account import update_user_name,update_user_password

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

    class Meta:
        model = User
        fields = ('email','password','first_name','last_name')
    
    def create(self, validated_data):
        user = create_user(validated_data)
        return user


class GetUserSerializer(serializers.ModelSerializer):
    

    class Meta:
        model = User
        fields = ('first_name', 'last_name' , 'id' , 'email' )



class RenameUserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = User
        fields = ( 'first_name' , 'last_name')

    def update(self, instance, validated_data):
        return update_user_name(
            user=instance,
            first_name=validated_data.get("first_name"),
            last_name=validated_data.get("last_name"),
        )


class ChangePasswordSerializer(serializer.Serializer):
    old_password = serializers.CharField(write_only=True)
    new_password = serializers.CharField(write_only=True)

    def update(self, instance, validated_data):
        
        return update_user_password(
            user=instance,
            old_password=validated_data["old_password"],
            new_password=validated_data["new_password"]
        )
    

