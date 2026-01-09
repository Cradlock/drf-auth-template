from django.contrib.auth.models import BaseUserManager
from apps.accounts.exceptions import EmailRequiredException,IncorrectCreateSuperUser


# Менеджер для управлением обьектов
class AccountManager(BaseUserManager):
    # Заставляет джанго использовать этот менеджер при миграциях
    use_in_migrations = True   

    # создание пользователя
    def create_user(self,email, password=None, **extra_fields):
        if not email:
            raise EmailRequiredException

        email = self.normalize_email(email)
        user = self.model(email=email,**extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user



    # Создания при помощи createsuperuser
    def create_superuser(self,email, password=None, **extra_fields):
        
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise IncorrectCreateSuperUser
        if extra_fields.get("is_superuser") is not True:
            raise IncorrectCreateSuperUser

        return self.create_user(email,password,**extra_fields)

    





