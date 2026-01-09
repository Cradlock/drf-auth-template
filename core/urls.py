
from django.contrib import admin
from django.urls import path,include,re_path

from django.conf import settings
from django.conf.urls.static import static

from rest_framework import permissions

from drf_yasg.views import get_schema_view
from drf_yasg import openapi

# Настройка swagger
schema_view = get_schema_view(
    openapi.Info(
      title="My Project API",
      default_version='v1',
      description="Документация по API",
      terms_of_service="https://www.example.com/terms/",
      contact=openapi.Contact(email="contact@example.com"),
      license=openapi.License(name="MIT License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,)
)


urlpatterns = [
    # Админ-панель
    path('admin/', admin.site.urls),

    # Подключенные приложения
    path('api/',include("apps.base.urls")),

    # Swagger UI
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]





if settings.DEBUG:
# медиа и cтатик файлы

    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

    urlpatterns += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
