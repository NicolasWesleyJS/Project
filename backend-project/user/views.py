from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets
from user.models import User
from user.serializers import UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    detail_serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]