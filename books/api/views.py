from rest_framework.viewsets import ModelViewSet
from .serializers import AuthorSerializer, BookAddSerializer
from author.models import Author
from .permissions import IsAuthorOrReadOnly
from book.models import Book


class AuthorViewSet(ModelViewSet):
    serializer_class = AuthorSerializer
    queryset = Author.objects.all()
    permission_classes = (IsAuthorOrReadOnly,)


class BookViewSet(ModelViewSet):
    serializer_class = BookAddSerializer
    queryset = Book.objects.all()
    permission_classes = (IsAuthorOrReadOnly,)

    def perform_create(self, serializer):
        print(serializer.data)
        serializer.save(authors=self.request.user)
