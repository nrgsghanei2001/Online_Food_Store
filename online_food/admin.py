from django.contrib import admin
from django.db.models.fields import CharField
from .models import *


class FoodInline(admin.TabularInline):
    model = Food


class BranchInline(admin.TabularInline):
    model = Branch


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']
    list_filter = ['name']
    search_fields = ['name']


@admin.register(Meal)
class MealAdmin(admin.ModelAdmin):
    list_display = ['meal']
    list_filter = ['meal']
    search_fields = ['meal']
    inlines = [FoodInline]


@admin.register(Restaurant)
class RestaurantAdmin(admin.ModelAdmin):
    list_display = ['name']
    list_filter = ['name']
    search_fields = ['name']
    inlines = [BranchInline]


@admin.register(Branch)
class BranchAdmin(admin.ModelAdmin):
    list_display = ['restaurant', 'menu_display']
    list_filter = ['restaurant']
    search_fields = ['restaurant']
    
    @admin.display(description='menu')
    def menu_display(self, obj):
        return " , ".join(ad.food.name for ad in obj.menu.all())


@admin.register(Food)
class FoodAdmin(admin.ModelAdmin):
    list_display = ['name', 'detail', 'category_list', 'meal']
    list_filter = ['name', 'meal']
    search_fields = ['name', 'meal']
    
    @admin.display(description='categories')
    def category_list(self, obj):
        return " , ".join(ad.name for ad in obj.category.all())


@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    list_display = ['food', 'price', 'number_of_existance']
    list_editable = ['price', 'number_of_existance']
    search_fields = ['price']
    

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['customer', 'restaurant', 'menu_list', 'customers_status', 'restaurnt_status']
    list_filter = ['customer', 'restaurant', 'customers_status', 'restaurnt_status']
    search_fields = ['customer', 'restaurant', 'customers_status', 'restaurnt_status']
    
    @admin.display(description='menu')
    def menu_list(self, obj):
        return " , ".join(ad.food.name for ad in obj.menu.all())


@admin.register(Invoice)
class InvoiceAdmin(admin.ModelAdmin):
    list_display = ['customer', 'last_purchase']
    list_filter = ['customer', 'last_purchase']
    search_fields = ['customer']


