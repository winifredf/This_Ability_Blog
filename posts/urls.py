from django.urls import path
from . import views
from django.urls import pattern, include,
from login.views import *

urlpatterns = [
    path('', views.index, name = 'index'),
    path('post/<str:pk>', views.post, name='post')
    path('register', views.register, name='register')
    path('login', views.login, name='login')
    path('logout', views.logout, name='logout')
]