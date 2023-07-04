from django.contrib import admin

from book.admin import AuthorInline

from .models import Author


class AuthorAdmin(admin.ModelAdmin):
    inlines = (AuthorInline,)
    list_display = (
        'id',
        'email',
        'first_name',
        'last_name',
    )
    list_filter = (
        'id',
        'email',
        'last_name',
    )
    search_fields = (
        'email',
        'last_name',
    )


admin.site.register(Author, AuthorAdmin)
