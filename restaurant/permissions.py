from .models import Staff


class BranchOperations:

    def has_perm_add_branch(self, request):
        staff = Staff.objects.filter(user=request.user)
        
        if staff:
            if not staff.first().restaurant:
                return True
            else:
                return False
        else:
            return False

    
    def has_perm_for_menu_or_orders(self, request):
        staff = Staff.objects.filter(user=request.user)
        
        if staff:
            return True
        else:
            return False

    
    def has_perm_for_edit(self, request):
        staff = Staff.objects.filter(user=request.user)
        
        if staff:
            if staff.first().restaurant.menu:
                return True
            else:
                return False
        else:
            return False
