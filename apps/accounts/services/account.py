from django.contrib.auth import get_user_model
from apps.accounts.exceptions import OldPasswordIncorrect


User = get_user_model()



def update_user_name(user: User, first_name: str, last_name: str) -> User:
    user.first_name = first_name
    user.last_name = last_name
    user.save(update_fields=["first_name", "last_name"])
    return user



def update_user_password(user: User, old_password: str, new_password: str) -> User:
    if not user.check_password(old_password):
        raise OldPasswordIncorrect

    user.set_password(new_password)
    user.save(update_fields=["password"])
    return user



