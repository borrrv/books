from django.db import models
from author.models import Author


class Book(models.Model):
    title = models.CharField(
        max_length=150,
    )
    archived = models.BooleanField(
        default=False,
    )
    authors = models.ManyToManyField(
        Author
    )

    def __str__(self):
        return self.title


class Comment(models.Model):
    author = models.ForeignKey(
        Author,
        on_delete=models.CASCADE,
        related_name='comment',
    )
    book = models.ForeignKey(
        Book,
        on_delete=models.CASCADE,
        related_name='comment'
    )
    text = models.CharField(
        max_length=400,
    )

    def __str__(self):
        return f"Комментарий {self.author} к книге {self.book}"
