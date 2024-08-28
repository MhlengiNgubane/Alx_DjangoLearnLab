from rest_framework.permissions import BasePermission


class IsAdminOrReadOnly(BasePermission):
    """
    Custom permission to allow only admin users to edit objects.
    """
    def has_permission(self, request, view):
        # Allow read-only access to everyone
        if request.method in ['GET', 'HEAD', 'OPTIONS']:
            return True
        # Allow write access only to admin users
        return request.user and request.user.is_staff