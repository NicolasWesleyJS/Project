from django.urls import path, include
from .views import ListAccounts, DetailAccounts

urlpatterns = [
    path('<int:pk>/', DetailAccounts.as_view()),
    path('', ListAccounts.as_view()),
]

