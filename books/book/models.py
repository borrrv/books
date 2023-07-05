from django.db import models

from author.models import Author


class Book(models.Model):
    """Модель для книг"""
    title = models.CharField(
        max_length=150,
        unique=True,
        verbose_name='Название',
    )
    text = models.TextField(
        verbose_name='Текст книги'
    )
    archived = models.BooleanField(
        default=False,
    )
    authors = models.ManyToManyField(
        Author,
        related_name='books'
    )

    class Meta:
        verbose_name = 'Книги'
        verbose_name_plural = 'Книги'

    def __str__(self):
        return self.title


class Comment(models.Model):
    """Модель комментариев"""
    author = models.ForeignKey(
        Author,
        on_delete=models.CASCADE,
        related_name='comment',
    )
    book = models.ForeignKey(
        Book,
        on_delete=models.CASCADE,
        related_name='comment',
    )
    text = models.CharField(
        max_length=400,
    )

    class Meta:
        verbose_name = 'Комментарии'
        verbose_name_plural = 'Комментарии'

    def __str__(self):
        return f"Комментарий {self.author} к книге {self.book}"
