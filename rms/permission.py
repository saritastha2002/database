from rest_framework.permissions import BasePermission
from rest_framework.permissions import SAFE_METHODS
class IsAuthenticationOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        return request.method== request.user and request.user.is_authenticated
        # return super().has_permission(request, view)(self,request,view)