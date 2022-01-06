from django.urls import path

from online_food.models import Invoice
from .views import *
from django.urls.conf import include, include
from django.conf import settings
from django.conf.urls.static import static
import os
from rest_framework import routers

# router = routers.DefaultRouter()
# router.register('add/food/admin', AddFood, basename='addFood')

urlpatterns = [
    # path('', include(router.urls)), 
    path('', home_page, name='home'),
    path('add/to/cart/', add_to_cart, name='add_to_cart'),
    path('all/restaurants/', AllRestaurants.as_view(), name='all_restaurants'),
    path('all/restaurants/<int:pk>', RestaurantDetail.as_view(), name='restaurants_detail'),
    path('all/restaurants/menu/<int:pk>', Menu.as_view(), name='restaurants_menu'),
    path('cart/', cart, name='cart'),
    path('invoices/', invoice, name='invoice'),
    path('all/foods/', AllFoods.as_view(), name='all_foods'),
    path('add/food/', add_food, name='add_food'),
    path('delete/item/', delete_item, name='delete_item'),
    path('delete/food/', delete_food, name='delete_food'),
    
    
    # path('popular/foods/', PopularFoods.as_view(), name='popular_foods'),
    
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT + os.path.altsep)


