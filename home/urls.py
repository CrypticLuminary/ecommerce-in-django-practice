from django.urls import path
from .views import *

urlpatterns = [
    path('', webpage.landingpage, name='landingpage'),
]
