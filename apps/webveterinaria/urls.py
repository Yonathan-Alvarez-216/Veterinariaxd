from django.urls import path
from .views import *

urlpatterns = [
    path('', kayu, name='index'),
]