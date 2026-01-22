import os 
import requests 
import httpx 

from google.oauth2 import id_token 
from google.auth.transport import requests 

GOOGLE_AUTH_URL = "https://accounts.google.com/o/oauth2/v2/auth"
GOOGLE_TOKEN_URL = "https://oauth2.googleapis.com/token"

# Google ключи 
GOOGLE_CLIENT_ID = os.getenv("GOOGLE_CLIENT_ID")
GOOGLE_CLIENT_SECRET = os.getenv("GOOGLE_CLIENT_SECRET")


from apps.accounts.exceptions import (
    GoogleTokenError,InvalidIdToken,MissingIdToken  
)


# Создание google логин ссылки
def generate_google_redirect(redirect_uri : str) -> str:
    
    params = {
        "client_id": GOOGLE_CLIENT_ID,
        "redirect_uri": redirect_uri,
        "response_type":"code",
        "scope":"openid email profile",
        "access_type":"offline",
        "prompt":"consent"
    }

    url = GOOGLE_AUTH_URL + "?" + "&".join(
        f"{k}={v}" for k, v in params.items()
    )

    return url 

# Обмен code и state на id_token
async def get_data(code : str, redirect_uri : str ,state : str = ""):
    data = {
        "code": code,
        "client_id": GOOGLE_CLIENT_ID,
        "client_secret": GOOGLE_CLIENT_SECRET,
        "redirect_uri": redirect_uri,
        "grant_type": "authorization_code"
    } 
    try:    
        async with httpx.AsyncClient() as client:
            response = await client.post(GOOGLE_TOKEN_URL, data=data)
            response.raise_for_status()
    except httpx.HTTPError:
        raise GoogleTokenError()
    
    except httpx.RequestError:
        raise GoogleTokenError()

    return response.json()


 
# вывод данных из response.json 
def decode_email_id_token(data : dict):
    
    if "id_token" not in data:
        raise MissingIdToken()
    
    try:
        idinfo = id_token.verify_oauth2_token(
            data.get("id_token"),
            requests.Request(),
            GOOGLE_CLIENT_ID 
        )
    
    except Exception:
        raise InvalidIdToken() 

    return idinfo.get("email",None)




    








