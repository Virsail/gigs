from django.conf.urls import url
from django.urls import path 
from .import views

urlpatterns = [
    path('register/', views.registerPage, name='register'),
    path('login/', views.loginPage, name='login'),
    path('', views.index, name='index')
]