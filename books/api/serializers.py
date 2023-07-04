from rest_framework import serializers

from author.models import Author
from book.models import Book, Comment


class AuthorShortInfoSerializer(serializers.ModelSerializer):
    """Короткая информация автора"""
    class Meta:
        model = Author
        fields = (
            'id',
            'first_name',
            'last_name',
        )


class AuthorSerializer(serializers.ModelSerializer):
    """Информация об авторе"""
    book_count = serializers.SerializerMethodField(read_only=True)
    comment_count = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Author
        fields = (
            'email',
            'first_name',
            'last_name',
            'book_count',
            'comment_count',
        )

    def get_book_count(self, obj):
        return obj.books.count()

    def get_comment_count(self, obj):
        return obj.comment.count()


class BookSerializer(serializers.ModelSerializer):
    """Информация о книгах"""
    authors = AuthorShortInfoSerializer(
        many=True,
        required=False,
    )
    comment_count = serializers.SerializerMethodField(read_only=True,)

    class Meta:
        model = Book
        fields = (
            'id',
            'title',
            'comment_count',
            'authors',
        )

    def create(self, validated_data):
        authors_data = validated_data.pop('authors', [])
        book = Book.objects.create(**validated_data)
        user = self.context['request'].user
        author = Author.objects.get(id=user.id)
        book.authors.add(author)
        for author_data in authors_data:
            author = Author.objects.get(**author_data)
            book.authors.add(author)
        return book

    def get_comment_count(self, obj):
        return obj.comment.count()


class BookPubSerializer(serializers.ModelSerializer):
    """Информация о книгах для публичного доступа"""

    class Meta:
        model = Book
        fields = (
            'title',
        )


class CommentSerializer(serializers.ModelSerializer):
    """Сериалайзер комментария"""

    class Meta:
        model = Comment
        fields = (
            'author',
            'book',
            'text',
        )
