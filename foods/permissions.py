from rest_framework import permissions


class AllFoods(permissions.BasePermission):

    def has_permission(self, request, view):
        if request.user.is_superuser:
            return True
        else:
            return False


class FoodOperations:
    
    def has_perm(self, request):
        if request.user.is_superuser:
            return True
        else:
            return False