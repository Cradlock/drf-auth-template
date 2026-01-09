
# Файл для создания пользовтеля
from django.contrib.auth import get_user_model

User = get_user_model()



def create_user( password : str , email : str ,first_name : str = "" , last_name : str = "") -> User:
    user = User.objects.create_user(

    )

    return user






