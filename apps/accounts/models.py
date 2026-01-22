from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from apps.accounts.managers import AccountManager




# Файл для базового пользователя
class Account(AbstractBaseUser,PermissionsMixin):
    class Roles(models.TextChoices):
        # Можно обновить
        client = 'client', 'Пользователь'
        support = 'support', 'Помощник'
        admin = 'admin', 'Админ'

    # Базовые поля: 
    first_name = models.CharField(max_length=255, blank=True)
    last_name = models.CharField(max_length=255,blank=True)
    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False) 
    is_superuser = models.BooleanField(default=False)

    email = models.EmailField(unique=True)
    role = models.CharField(max_length=20,choices=Roles.choices)
    
    objects = AccountManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email





