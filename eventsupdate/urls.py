from django.conf.urls import url, include
from . import views
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static 

# app_name = 'eventsupdate'

urlpatterns = [
    url(r'^$', views.event_today, name = 'eventsToday'),
    url(r'^search/$', views.search_results, name='search_results'),
    url(r'^event/(\d+)',views.event,name ='event'),
    url(r'^new/event$', views.new_event, name='new-event'),
    url(r'^ajax/eventletter/$', views.eventletter, name='eventletter')  
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,  document_root=settings.STATIC_ROOT)

    

