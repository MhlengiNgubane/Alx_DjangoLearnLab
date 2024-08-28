from django.urls import include, path
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework.routers import DefaultRouter

from .views import BookViewSet

router = DefaultRouter()
router.register(r'books', BookViewSet)

urlpatterns = [
    # Endpoint for obtaining authentication tokens
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
    # Include router URLs
    path('', include(router.urls)),
]