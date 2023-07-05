from django.shortcuts import get_object_or_404
from djoser.views import UserViewSet
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.status import (HTTP_201_CREATED, HTTP_202_ACCEPTED,
                                   HTTP_400_BAD_REQUEST,
                                   HTTP_405_METHOD_NOT_ALLOWED)
from rest_framework.viewsets import ModelViewSet

from author.models import Author
from book.models import Book, Comment

from .permissions import IsAuthorOrReadOnly
from .serializers import (AuthorSerializer, BookPubSerializer, BookSerializer,
                          CommentSerializer)


class AuthorViewSet(UserViewSet):
    """Вьюсет для работы с авторами"""
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    permission_classes = (IsAuthorOrReadOnly, )


class BookViewSet(ModelViewSet):
    """ВЬюсет для работы с книгами и создания комментариев"""
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = (IsAuthorOrReadOnly,)

    @action(detail=True, methods=['get'])
    def authors(self, request, pk=None):
        author = get_object_or_404(Author, pk=pk)
        books = Book.objects.filter(archived=False, authors=author)
        serializer = BookPubSerializer(books, many=True)
        return Response(serializer.data)

    @action(detail=True, methods=['patch'])
    def archived(self, requset, pk=None):
        archived = get_object_or_404(Book, pk=pk)
        new_archived = bool(self.request.data['archived'])
        if archived:
            if archived.archived == new_archived:
                content = {
                    'message':
                    f'Состояние не изменилось, осталось {new_archived}'
                }
                return Response(content, status=HTTP_400_BAD_REQUEST)
            else:
                archived.archived = new_archived
                archived.save()
                content = {
                    'message': f'Статус книги изменен на {new_archived}'
                }
                return Response(content, status=HTTP_202_ACCEPTED)
        else:
            content = {"message": "Передайте обязательный параметр 'archived'"}
            return Response(content, status=HTTP_400_BAD_REQUEST)

    @action(detail=True, methods=['post'])
    def comment(self, request, pk=None):
        book = get_object_or_404(Book, pk=pk)
        user = self.request.user
        if request.method == 'POST':
            text = request.data['text']
            comment = Comment.objects.create(
                author_id=user.id,
                book=book,
                text=text,
            )
            serializer = CommentSerializer(
                comment,
                context={'request': request},
            )
            return Response(serializer.data, status=HTTP_201_CREATED)


class CommentViewSet(ModelViewSet):
    """Вьюсет для обновления и удаления комментариев"""
    serializer_class = CommentSerializer
    permission_classes = (IsAuthorOrReadOnly, )

    def get_queryset(self):
        user = self.request.user
        return Comment.objects.filter(author=user)

    def create(self, request, *args, **kwargs):
        return Response(status=HTTP_405_METHOD_NOT_ALLOWED)
