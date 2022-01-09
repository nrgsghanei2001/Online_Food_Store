from django.contrib import admin
from .models import *


@admin.register(Staff)
class StaffAdmin(admin.ModelAdmin):
    list_display = ['user', 'email', 'staff_info']
    list_editable = ['email']

    @admin.display(description='staff info')
    def staff_info(self, obj):
        return " , ".join(ad.address for ad in obj.address.all())