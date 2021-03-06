from django.conf.urls import url, include
from . import views
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static 

# app_name = 'eventsupdate'

urlpatterns = [
    url(r'^registerPage/$', views.registerPage, name='registerPage'),
    url(r'^$', views.event_today, name = 'eventsToday'),
    url(r'^search/$', views.search_results, name='search_results'),
    url(r'^archives/(\d{4}-\d{2}-\d{2})/$',views.show_events,name = 'showEvents'),
    url(r'^event/(\d+)',views.event,name ='event'),
    url(r'^new/event$', views.new_event, name='new-event'),
    url(r'^ajax/eventsletter/$', views.eventletter, name='eventsletter')  
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
