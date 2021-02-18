from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include('apps.user.urls')),
    path('finances/', include('apps.finance.urls')),
    path('api/', include('apps.api.urls')),
]
