

from rest_framework.views import APIView 

from rest_framework.response import Response 

from apps.accounts.services import (
    generate_google_redirect,get_data,
    get_or_create_user,decode_email_id_token,
    issue_jwt_tokens 
)

from rest_framework import status 


from apps.accounts.serializers import (
    GetGoogleRedirectSerializer,
    GoogleLoginSerializer 
)


class GoogleAuthView(APIView):
    

    async def get(self,request):
        
        seriliazer = GetGoogleRedirectSerializer(data=request.query_params)
        seriliazer.is_valid(raise_exception=True)
        
        redirect_uri = seriliazer.validated_data["redirect_uri"] 
        rurl = generate_google_redirect(redirect_uri)
        return Response(
            {"redirect_uri":rurl},status=status.HTTP_200_OK
        )

    async def post(self,request):

        serializer = GoogleLoginSerializer(data=request.data)
        
        serializer.is_valid(raise_exception=True)

        code = serializer.validated_data.get("code",None)
        redirect_uri = serializer.validated_data.get("redirect_uri",None)
        
        data = await get_data(code,redirect_uri)
        email = decode_email_id_token(data)
        
        user = get_or_create_user(email)
        response = Response()
        return issue_jwt_tokens(user,response)





