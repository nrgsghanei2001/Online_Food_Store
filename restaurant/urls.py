from django.urls import path
from .views import *
from django.urls.conf import include, include
from django.conf import settings
from django.conf.urls.static import static
import os



urlpatterns = [
    path('register/staff/', register, name='register_staff'),
    path('add/branch/', add_branch, name='add_branch'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT + os.path.altsep)


