from django.contrib import admin
from .models import *

@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    list_display = ['city', 'address', 'phone']
    list_display_links = ['city']
    list_editable = ['phone']
    list_filter = ['city']
    search_fields = ['city']


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['users', 'email', 'user_info']
    list_editable = ['email']

    @admin.display(description='user')
    def users(self, obj):
        if obj.user:
            return obj.user.username
        else:
            return obj.device

    @admin.display(description='user info')
    def user_info(self, obj):
        return " , ".join(ad.address for ad in obj.address.all())


@admin.register(Staff)
class StaffAdmin(admin.ModelAdmin):
    list_display = ['user', 'email', 'staff_info']
    list_editable = ['email']

    @admin.display(description='staff info')
    def staff_info(self, obj):
        return " , ".join(ad.address for ad in obj.address.all())

