from rest_framework import generics, viewsets
from .models import Account
from .serializers import AccountSerializer

class ListAccounts(generics.ListCreateAPIView):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer

class DetailAccounts(generics.RetrieveUpdateDestroyAPIView):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer

