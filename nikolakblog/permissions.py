from rest_framework import permissions
from cms.models import Author


def is_authenticated(request):
    return bool(request.user and request.user.is_authenticated)


class IsBlogAuthorOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):

        if request.method == 'OPTIONS':
            return True

        if not bool(request.user and request.user.is_authenticated):
            return False

        if request.method in permissions.SAFE_METHODS.append('POST') and is_staff_member(request.user):
            return True

        return request.method in permissions.SAFE_METHODS and is_volunteer(request.user)