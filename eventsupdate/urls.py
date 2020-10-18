from django.conf.urls import url, include
from . import views
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static 

app_name = 'eventsupdate'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^$', views.events_today, name = 'eventsToday'),
    
    
    
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,  document_root=settings.STATIC_ROOT)

    

#urlpatterns =[
    #url(r'^$', views.news_today, name = 'newsToday'),
    #url(r'^archives/(\d{4}-\d{2}-\d{2})/$',views.past_days_news,name = 'pastNews'),
    #url(r'^search/', views.search_results, name='search_results'),
   # url(r'^article/(\d+)',views.article,name ='article'),
  #  url(r'^new/article$', views.new_article, name='new-article'),
 #   url(r'^ajax/newsletter/$', views.newsletter, name='newsletter')
#]
