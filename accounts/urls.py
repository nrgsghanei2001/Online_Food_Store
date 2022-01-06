from django.urls import path
from .views import *


urlpatterns = [
    path('signup/', SignupPageView, name='signup'),
    path('register/', register, name='register'),
]