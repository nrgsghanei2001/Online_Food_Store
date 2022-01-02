from django.urls import path
from .views import *
from django.contrib.staticfiles.urls import static
from final_project import settings

urlpatterns = [
    path('', home_page, name='home'),
    path('add/food/', add_food, name='add_food'),
    path('all/restaurants/', AllRestaurants.as_view(), name='all_restaurants'),
    path('all/restaurants/<int:pk>', RestaurantDetail.as_view(), name='restaurants_detail'),
    path('all/restaurants/menu/<int:pk>', Menu.as_view(), name='restaurants_menu'),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


