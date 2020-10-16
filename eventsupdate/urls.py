from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$register/', views.registerPage, name='register'),
    url(r'^$login/', views.loginPage, name='login'),
    url(r'^$logout/', views.logoutUser, name='logout'),
    url(r'^$', views.index, name='index')
]