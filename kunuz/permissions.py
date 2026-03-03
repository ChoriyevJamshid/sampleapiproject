from rest_framework.permissions import BasePermission


class IsOwnerPermission(BasePermission):

    message = "Sizda ruxsat yoq."

    def has_object_permission(self, request, view, obj):

        if not hasattr(obj, 'author'):
            return True

        if obj.author == request.user:
            return True
        return False




