from .views import UserViewSet
from rest_framework import routers
from django.urls import path, include

app_name = 'user'
router = routers.DefaultRouter()
router.register('api', UserViewSet)

urlpatterns = [
    path('', include(router.urls))
]