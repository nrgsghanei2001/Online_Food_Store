from django.contrib import admin
from django.db.models.fields import CharField
from .models import *


class FoodInline(admin.TabularInline):
    model = Food


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


@admin.register(Food)
class FoodAdmin(admin.ModelAdmin):
    list_display = ['name', 'detail', 'category_list', 'meal']
    list_filter = ['name', 'meal']
    search_fields = ['name', 'meal']
    
    @admin.display(description='categories')
    def category_list(self, obj):
        return " , ".join(ad.name for ad in obj.category.all())