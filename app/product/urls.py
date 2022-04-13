from rest_framework import routers
from django.urls import path, include
from django.contrib.auth.models import User

from .views import *

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'product', ProductViewset)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
