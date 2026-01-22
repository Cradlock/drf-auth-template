from django.contrib.auth import get_user_model
from apps.accounts.exceptions import OldPasswordIncorrect


User = get_user_model()



def update_user_name(*,user: User, first_name: str, last_name: str) -> User:
    user.first_name = first_name
    user.last_name = last_name
    user.save(update_fields=["first_name", "last_name"])
    return user



def update_user_password(*,user: User, old_password: str, new_password: str) -> User:
    if not user.check_password(old_password):
        raise OldPasswordIncorrect

    user.set_password(new_password)
    user.save(update_fields=["password"])
    return user




def activate_user(user) -> User:
    if not user.is_active:
        user.is_active = True
        user.save()

    return User 


def create_user(
    *,
    email : str,
    password : str,
    role : str = User.roles.client,
    is_active : bool = True,
    first_name : str = "",
    last_name : str = ""
) -> User:
    user = User.objects.create_user(
        email=email,
        password=password,
        role=role,
        is_active=is_active,
        first_name=first_name,
        last_name=last_name
    ) 

    return user 





def get_or_create_user(
    *,
    email : str,
    password : None
) -> User:
    user, created = User.objects.get_or_create(
        email=email,
        defaults={
            "is_active": True,
            "role": User.Roles.client,
            "password": password 
        },
    )
    
    if not user.is_active:
        user.is_active = True
        user.save(update_fields=["is_active"])
    
    return user 










