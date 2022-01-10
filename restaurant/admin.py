from django.contrib import admin
from .models import *


@admin.register(Staff)
class StaffAdmin(admin.ModelAdmin):
    list_display = ['user', 'email', 'restaurant']
    list_editable = ['email']
