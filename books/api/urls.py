from django.urls import path, include
from .views import AuthorViewSet, BookViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register('author', AuthorViewSet)
router.register('book', BookViewSet)

urlpatterns = (
    path('', include(router.urls)),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),
)
