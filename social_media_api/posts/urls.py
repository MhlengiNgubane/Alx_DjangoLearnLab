from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import CommentViewSet, FeedView, PostViewSet

router = DefaultRouter()
router.register(r'posts', PostViewSet)
router.register(r'comments', CommentViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('feed/', FeedView.as_view(), name='feed'),
]