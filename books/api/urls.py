from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import AuthorViewSet, BookViewSet, CommentViewSet

router = DefaultRouter()
router_auth = DefaultRouter()

router.register('books', BookViewSet)
router.register('comments', CommentViewSet, basename='comments')
router_auth.register('authors', AuthorViewSet)

urlpatterns = (
    path('', include(router.urls)),
    path('auth/', include(router_auth.urls)),
    path('auth/', include('djoser.urls.jwt')),
)
