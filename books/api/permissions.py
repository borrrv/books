from rest_framework.permissions import SAFE_METHODS, BasePermission


class IsAuthorOrReadOnly(BasePermission):

    def has_permission(self, request, view):
        return request.user.is_authenticated or request.method in SAFE_METHODS

    def has_object_permission(self, request, view, obj):
        print(request.user.id)
        print(obj.authors.all())
        return (request.user in obj.authors.all()
                or request.method in SAFE_METHODS)
