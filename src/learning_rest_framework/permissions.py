from rest_framework import permissions


class IsOwnerOrReadOnlySnippet(permissions.BasePermission):
    """
    Custom permission to only allow owners of an object to edit it.
    """

    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        if not request.method in permissions.SAFE_METHODS:
            return False

        # Write permissions are only allowed to the owner of the snippet.
        return obj.owner == request.user