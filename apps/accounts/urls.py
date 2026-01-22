
from django.urls import path
from .views import (
    RefreshAPIView,
    LogoutAPIView,
    LoginAPIView,
    GoogleAuthView,
    AccountViewSet,
    ActivateAccountAPIView 

)

from rest_framework.routers import DefaultRouter 

router = DefaultRouter()
router.register(r"account",AccountViewSet, basename="account")

urlpatterns = [

    # Логин 
    path("login/",LoginAPIView.as_view(),name="login"),

    # Обновление access
    path("refresh/",RefreshAPIView.as_view(),name="refresh"),

    # Выход из аккаунта
    path("logout/",LogoutAPIView.as_view(),name="logout" ),
    
    # Активация аккаунта 
    path("activate/",ActivateAccountAPIView.as_view(),name="activate-account"),

    # Авторизация через соц аккаунты 
     # Google 
    path("google/",GoogleAuthView.as_view(),name="google-auth"),
    
]


urlpatterns += router.urls



