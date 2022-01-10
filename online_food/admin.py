from django.contrib import admin
from django.db.models.fields import CharField
from .models import *


class BranchInline(admin.TabularInline):
    model = Branch


@admin.register(Restaurant)
class RestaurantAdmin(admin.ModelAdmin):
    list_display = ['name']
    list_filter = ['name']
    search_fields = ['name']
    inlines = [BranchInline]


@admin.register(Branch)
class BranchAdmin(admin.ModelAdmin):
    list_display = ['restaurant', 'date_of_register_jalali']
    list_filter = ['restaurant']
    search_fields = ['restaurant']
    


@admin.register(MenuItem)
class MenuItemAdmin(admin.ModelAdmin):
    list_display = ['food', 'price', 'number_of_existance']
    list_editable = ['price', 'number_of_existance']
    list_filter = ['food', 'price', 'number_of_existance']
    search_fields = ['food', 'price', 'number_of_existance']


@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    list_display = ['items', 'restaurant']
    

    @admin.display(description='menu items')
    def items(self, obj):
        return " , ".join(ad.food.name for ad in obj.item.all())

    @admin.display(description='related restaurant')
    def restaurant(self, obj):
        return obj.branches
    

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['customer', 'restaurant', 'customers_status', 'restaurant_status']
    list_filter = ['customer', 'restaurant', 'customers_status', 'restaurant_status']
    search_fields = ['customer', 'restaurant', 'customers_status', 'restaurant_status']


@admin.register(Invoice)
class InvoiceAdmin(admin.ModelAdmin):
    list_display = ['customer', 'last_purchase_jalali']
    list_filter = ['customer']
    search_fields = ['customer']


admin.site.register(OrderItem)
