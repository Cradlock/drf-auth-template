
from rest_framework_simplejwt.tokens import RefreshToken
from django.utils.http import urlsafe_base64_encode 
from django.contrib.auth.tokens import default_token_generator 

from django.conf import settings 
from django.utils.encoding import force_bytes 

from django.contrib.auth import get_user_model 


User = get_user_model()


def issue_jwt_tokens(user, response):
    refresh = RefreshToken.for_user(user)

    response.set_cookie(
        key="refresh",
        value=str(refresh),
        **settings.REFRESH_TOKEN_PARAMETERS
    )

    response.data = {
        "access": str(refresh.access_token)
    }

    return response











def generate_link_for_active_user(*,
    user : User,domain : str
) -> str:
    
    uidb64 = urlsafe_base64_encode(force_bytes(user.pk))
    
    token = default_token_generator.make_token(user) 
    
    return f"{domain}?uidb64={uidb64}&token={token}"











