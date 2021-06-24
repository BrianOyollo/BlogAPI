from rest_framework import permissions


class IsAuthorOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        """ Read-only permissions will be allowed for all requests."""
        if request.method in permissions.SAFE_METHODS:
            return True
        """ Write permissions(create & edit) will be allowed to the author of the post """
        return obj.author == request.user
