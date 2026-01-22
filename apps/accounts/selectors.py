
# Файл для выборки и получения обьекта User
from django.contrib.auth import get_user_model 
from apps.accounts.exceptions import UserNotFound 

User = get_user_model()

def get_user_by_id(uid) -> User:
    try:
        user = User.objects.get(id=uid)
        return user
    except (ValueError,TypeError,User.DoesNotExists):
        raise UserNotFound()










