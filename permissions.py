from rest_framework import permissions

from users.models import User


class IsSelectionOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if obj.user == request.user:
            return True
        return False


class UserAndRoleVerification(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if obj.author == request.user:
            return True
        return False


    def has_permission(self, request, view):
        if request.user.role in ["admin", "moderator"]:
            return True
        return False