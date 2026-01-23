


from rest_framework import status,viewsets 
from rest_framework.permissions import IsAuthenticated 
from rest_framework.decorators import action 
from rest_framework.response import Response 

from apps.accounts.serializers import (
    ChangePasswordSerializer,
    GetUserSerializer,
    RenameUserSerializer,
    RegisterUserSerializer 
)

from apps.accounts.services import (
    update_user_name,update_user_password,create_user,generate_link_for_active_user 
)

from apps.base.utils import send_email 

from apps.accounts.selectors import get_user_by_email 

from apps.accounts.exceptions import EmailAndFrontendDomainRequired 

# Создания обновление изменения
class AccountViewSet(viewsets.ViewSet):
    
    def get_permissions(self):  
        if self.action in ["create","repeat_email"]:
            return []
        return [IsAuthenticated,]

    # action change name
    @action(detail=False,methods=["put"])
    def change_name(self,request):
        serializer = RenameUserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        update_user_name(
            user=request.user, 
            **serializer.validated_data
        )

        return Response(serializer.validated_data,status=status.HTTP_200_OK)

    # action change password 
    @action(detail=False,methods=["put"])
    def change_password(self,request):
        serializer = ChangePasswordSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        update_user_password(
            user=request.user,
            **serializer.validated_data
        )

        return Response({"detail":"Ok"},status=status.HTTP_200_OK)


    # retrieve (/me function get info)
    @action(detail=False,methods=["get"])
    def me(self,request):
        serializer = GetUserSerializer(instance=request.user)
        return Response(serializer.data,status=status.HTTP_200_OK)

    # create - signup (no activated account )
    def create(self,request):
        serializer = RegisterUserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        frontend_domain = serializer.validated_data.pop("frontend_url")

        user = create_user(**serializer.validated_data)
        

        # send email for active account  
        activate_url = generate_link_for_active_user(user=user,domain=frontend_domain)
        email = user.email 

        send_email.delay(
            template_name="emails/confirm.html",
            data={
                "email":email,
                "activate_url":activate_url 
            },
            subject="Активация аккаунта",
            to_email=email 
        )

        return Response({"detail":"Ok"},status=status.HTTP_200_OK)
    
   
    @action(detail=False, methods=["post"], url_path="repeat-email")
    def repeat_email(self, request):
        serializer = RepeatEmailSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = get_user_by_email(serializer.validated_data["email"])
        activate_url = generate_link_for_active_user(
            user=user,
            domain=serializer.validated_data["frontend_domain"]
        )
        email = user.email 

        send_email.delay(
            template_name="emails/confirm.html",
            data={
                "email":email,
                "activate_url":activate_url 
            },
            subject="Активация аккаунта",
            to_email=email 
        )


        return Response({"detail": "Ok"}, status=status.HTTP_201_CREATED)


