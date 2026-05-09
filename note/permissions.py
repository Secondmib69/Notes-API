from rest_framework.permissions import SAFE_METHODS, BasePermission
from .models import Note


class IsNoteUserOrStaffReadOnly(BasePermission):
    
    def has_object_permission(self, request, view, obj):
        return bool((request.user and request.user.is_superuser) or
                    (request.user and request.user == obj.user) or
                    (request.method in SAFE_METHODS and request.user and request.user.is_staff))
    

class IsSuperUserOrStaffReadOnly(BasePermission):

    def has_permission(self, request, view):
        return bool(
            (request.user and request.user.is_superuser) or
            (request.method in SAFE_METHODS and request.user and request.user.is_staff)
        )