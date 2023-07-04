from django.contrib import admin

from .models import Book, Comment


class AuthorInline(admin.TabularInline):
    model = Book.authors.through


class BookAdmin(admin.ModelAdmin):

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
    list_display = (
        'id',
        'text',
        'author',
        'book',
    )
    list_filter = (
        'author',
        'book',
    )


admin.site.register(Book, BookAdmin)
admin.site.register(Comment, CommentAdmin)
