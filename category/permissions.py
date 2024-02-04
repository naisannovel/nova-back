from rest_framework.permissions import BasePermission


class CustomIsAdminUser(BasePermission):
    def has_permission(self, request, view):
        if request.user.email == 'out@mail.com':
            return True
        return False


