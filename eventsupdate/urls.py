from django.conf.urls import url, include
from .import views
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static 

app_name = 'eventsupdate'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^$register', views.registerPage, name='register'),
    url(r'^$login/', views.loginPage, name='login'),
    url(r'^$logout/', views.logoutUser, name='logout'),    
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,  document_root=settings.STATIC_ROOT)
