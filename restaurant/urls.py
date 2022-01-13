from django.urls import path
from .views import *
from django.urls.conf import include, include
from django.conf import settings
from django.conf.urls.static import static
import os



urlpatterns = [
    path('register/staff/', register, name='register_staff'),
    path('add/branch/', add_branch, name='add_branch'),
    path('show/menu/', show_menu, name='show_menu'),
    path('add/to/menu/', add_to_menu, name='add_to_menu'),
    path('show/restaurants/orders/', show_restaurants_orders, name='show_restaurants_orders'),
    path('edit/item/', edit, name='edit_item'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT + os.path.altsep)


