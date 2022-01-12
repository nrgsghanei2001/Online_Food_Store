from django.urls import path
from .views import *
from django.urls.conf import include, include
from django.conf import settings
from django.conf.urls.static import static
import os
from rest_framework import routers


urlpatterns = [
    path('all/foods/', AllFoods.as_view(), name='all_foods'),
    path('add/food/', add_food, name='add_food'),
    path('add/category/', add_category, name='add_category'),
    path('delete/food/', delete_food, name='delete_food'),   
    path('edit/food/', edit_food, name='edit_food'),   
    path('edit/', edit, name='edit'),     
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT + os.path.altsep)


