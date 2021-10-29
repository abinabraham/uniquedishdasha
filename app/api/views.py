from django.urls import path, include
from rest_framework import routers, serializers, viewsets
from app.accounts.models import CustomUser, Branch
from .serializers import UserSerializer

# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer