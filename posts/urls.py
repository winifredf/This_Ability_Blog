from pipes import Template
from django import template, templatetags
from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name= 'index'),
    path('/post', views.post,),
    path('post/<str:pk>', views.post, name='post'),
    path('/login', views.login, name= 'login'),
    path('/logout', views.logout, name= 'logout'),
    path('/signup', views.signup, name= 'signup'),
    ]