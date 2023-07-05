from rest_framework.permissions import SAFE_METHODS, BasePermission
from book.models import Comment, Book


class IsAuthorOrReadOnly(BasePermission):

    def has_permission(self, request, view):
        return request.user.is_authenticated or request.method in SAFE_METHODS

    def has_object_permission(self, request, view, obj):
        if isinstance(obj, Comment):
            return (request.user == obj.authors
                    or request.method in SAFE_METHODS)
        elif isinstance(obj, Book):
            return (request.user in obj.authors.all()
                    or request.method in SAFE_METHODS)
        else:
            return False
