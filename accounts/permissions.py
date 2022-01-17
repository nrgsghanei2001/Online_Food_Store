from .models import Customer

class EditInfo:

    def has_perm(self, request):
        if request.user.is_superuser:
            return True
        else:
            user = Customer.objects.filter(user=request.user)
            if user:
                return True
            else:
                return False