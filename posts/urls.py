from pipes import Template
from django import template, templatetags
from django.urls import path
from django.urls import path, include
from django.contrib import admin
from . import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('posts.urls')) 
    path('', views.index, name= 'index'),
    #path('/post', views.post,),
    path('post/<str:pk>', views.post, name='post'),
    path('/login', views.login, name= 'login'),
    path('/logout', views.logout, name= 'logout'),
    path('/signup', views.signup, name= 'signup'),
    ]