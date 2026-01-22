

from rest_framework.views import APIView 

from rest_framework.response import Response 

from apps.accounts.services import (
    generate_google_redirect,get_data,
    get_or_create_user,decode_email_id_token,
    issue_jwt_tokens 
)

from rest_framework import status 

from apps.accounts.exceptions import (
    DontSendRedirectUri,MissingCodeOrRedirectUri  
)


class GoogleAuthView(APIView):
    

    async def get(self,request):
        redirect_uri = request.GET.get("redirect_uri",None)
        if redirect_uri is None:
            raise DontSendRedirectUri()

        rurl = generate_google_redirect(redirect_uri)
        return Response(
            {"redirect_uri":rurl},status=status.HTTP_200_OK
        )

    async def post(self,request):
        code = request.data.get("code",None)
        redirect_uri = request.data.get("redirect_uri",None)

        if not code or not redirect_uri:
            raise MissingCodeOrRedirectUri()
        
        data = await get_data(code,redirect_uri)
        email = decode_email_id_token(data)
        user = get_or_create_user(email)
        response = Response()
        return issue_jwt_tokens(user,response)









