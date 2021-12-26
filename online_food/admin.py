from django.contrib import admin
from django.db.models.fields import CharField
from .models import *


admin.site.register(Category)
admin.site.register(Restaurant)
