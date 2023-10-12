from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token
from .views import *

urlpatterns = [
    path('get_token/', GetTokenAPI.as_view()),
    path('goods/', view_goods, name='goods'),
    path('new_good/', new_good, name='new_good')
]
