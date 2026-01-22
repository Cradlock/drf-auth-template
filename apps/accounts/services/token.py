
from rest_framework_simplejwt.tokens import RefreshToken
from django.conf import settings

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





















