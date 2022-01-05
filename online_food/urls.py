from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static
import os

urlpatterns = [
    path('', home_page, name='home'),
    path('add/food/', add_to_cart, name='add_to_cart'),
    path('all/restaurants/', AllRestaurants.as_view(), name='all_restaurants'),
    path('all/restaurants/<int:pk>', RestaurantDetail.as_view(), name='restaurants_detail'),
    path('all/restaurants/menu/<int:pk>', Menu.as_view(), name='restaurants_menu'),
    path('cart/', Cart.as_view(), name='cart'),
    
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT + os.path.altsep)


