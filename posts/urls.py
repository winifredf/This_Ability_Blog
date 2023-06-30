from pipes import Template
from django import template, templatetags
from django.urls import path
from . import views
#from django.urls import include


urlpatterns = [
    path('', views.index, name = 'index'),
    path('post/<str:pk>', views.post, name='post'),
    path('login', views.login),
    path('logout', views.logout),
    path('signup', views.signup),

    path('register', template.register, name='register'),
    path('login', templatetags.login.html, name='login'),
    path('logout', Template.logout, name='logout'),
    ]