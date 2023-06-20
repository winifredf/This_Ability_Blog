from django.urls import path

urlpatters = [
    path('', views.index, name = 'index')
]