from django.urls import path
from .views import *
from django.urls.conf import include, include
from django.conf import settings
from django.conf.urls.static import static
import os


urlpatterns = [
    path('', home_page, name='home'),
    path('adminpannel/', admin_page, name='admin_page'),
    path('all/restaurants/', AllRestaurants, name='all_restaurants'),
    path('all/restaurants/<int:pk>', RestaurantDetail.as_view(), name='restaurants_detail'),
    path('all/restaurants/menu/<int:pk>', Menu.as_view(), name='restaurants_menu'),
    path('cart/', cart, name='cart'),
    path('add/to/cart/', add_to_cart, name='add_to_cart'),
    path('invoices/', invoice, name='invoice'),
    path('delete/item/', delete_item, name='delete_item'),
    path('all/orders/', all_orders, name='all_orders'),
    path('show/all/foods/', show_all_foods, name='show_all_foods'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT + os.path.altsep)


