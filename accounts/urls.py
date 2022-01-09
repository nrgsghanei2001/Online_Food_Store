from django.urls import path
from .views import *


urlpatterns = [
    path('signup/', SignupPageView, name='signup'),
    path('register/', register, name='register'),
    path('profile/', profile, name='profile'),
    path('edit/info/', edit_info, name='edit_info'),
    path('remove/address/', remove_address, name='remove_address'),
]