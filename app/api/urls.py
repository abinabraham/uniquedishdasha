from django.urls import path, include
from rest_framework import routers, serializers, viewsets
from app.accounts.models import CustomUser, Branch
from .views import UserViewSet

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('v1/', include(router.urls)),
]