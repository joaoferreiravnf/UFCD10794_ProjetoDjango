from django.contrib import admin
from django.urls import path,include 
from rest_framework.schemas import get_schema_view 
from django.views.generic import TemplateView 



urlpatterns = [
    path('adminapi/',include('AdminAPI.urls')),
    path('admin/', admin.site.urls),
    path('openapi/', get_schema_view(
        title="School Service",
        description="API for developers who would love to use our service in a School project"
        ), name='openapi-schema'),
    path('docs/', TemplateView.as_view(
        template_name='documentation.html',
        extra_context={'schema_url':'openapi-schema'}
        ), name='swagger-ui'),
    path('', TemplateView.as_view(
        template_name='documentation.html',
        extra_context={'schema_url':'openapi-schema'}
        ), name='swagger-ui'),
]