from django.urls import include,path 

# Сборка всего приложения


urlpatterns = [
    path("auth/",include("apps.accounts.urls"))
]

