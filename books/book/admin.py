from django.contrib import admin

from .models import Book, Comment


class AuthorInline(admin.TabularInline):
    model = Book.authors.through


class BookAdmin(admin.ModelAdmin):
    """Админка,связанная с книгами"""

    inlines = (AuthorInline,)

    list_display = (
        'id',
        'title',
        'archived',
    )

    list_filter = (
        'title',
        'authors',
        'archived',
    )
    search_fields = (
        'title',
    )


class CommentAdmin(admin.ModelAdmin):
    """Админка, связанная с комментариями"""
    list_display = (
        'id',
        'text',
        'authors',
        'book',
    )
    list_filter = (
        'authors',
        'book',
    )


admin.site.register(Book, BookAdmin)
admin.site.register(Comment, CommentAdmin)
