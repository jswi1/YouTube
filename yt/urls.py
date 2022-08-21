from drf_yasg import openapi
from django.contrib import admin
from rest_framework import permissions
from django.urls import path
from drf_yasg.views import get_schema_view



schema_view = get_schema_view(
   openapi.Info(
      title="Spotify API",
      default_version='v1',
      description="Bu loyiha Spotify API kloni sifatida ishlatilishi mumkin",
      contact=openapi.Contact("Muhammadqodir, Email: <>"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)



urlpatterns = [
    path('admin/', admin.site.urls),
   path('', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-doc'),
]
