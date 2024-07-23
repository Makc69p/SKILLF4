from django.contrib import admin
from django.urls import path, include
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('urls')),
]
schema_view = get_schema_view(
    openapi.Info(
        title="Recipe API",
        default_version='v1',
        description="API documentation for recipe app",
    ),
    public=True,
)

urlpatterns += [
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]