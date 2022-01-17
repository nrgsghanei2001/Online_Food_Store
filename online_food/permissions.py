from re import T
from accounts.models import Customer


class AdminPannel:

    def has_perm(self, request):
        if request.user.is_superuser:
            return True
        else:
            return False


class CartOperations:

    def has_perm(self, request):
        device = request.COOKIES['device']
        user, user_vir = [], []
        try:
            user = Customer.objects.filter(user=request.user)
        except:
            user_vir = Customer.objects.filter(device=device)
        if user:
            return True
        elif user_vir:
            return True
        else:
            return False

    def has_perm_logged_in(self, request):
        user = Customer.objects.filter(user=request.user)
        if user:
            return True
        else:
            return False