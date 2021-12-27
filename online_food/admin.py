from django.contrib import admin
from django.db.models.fields import CharField
from .models import *


admin.site.register(Category)
admin.site.register(Meal)
admin.site.register(Restaurant)
admin.site.register(Branch)
admin.site.register(Food)
admin.site.register(Menu)
admin.site.register(Order)
admin.site.register(Invoice)

