from rest_framework import serializers
from author.models import Author
from book.models import Book


class AuthorShortInfoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Author
        fields = (
            'first_name',
            'last_name',
        )


class AuthorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Author
        fields = (
            'username',
            'first_name',
            'last_name',
        )


class BookAddSerializer(serializers.ModelSerializer):
    authors = AuthorShortInfoSerializer(many=True, read_only=True)

    class Meta:
        model = Book
        fields = (
            'title',
            'authors',
        )
