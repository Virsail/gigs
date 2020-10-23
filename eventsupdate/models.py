from django.db import models
import datetime as dt
from django.contrib.auth.models import User
from tinymce.models import HTMLField

# Create your models here.
class EventOrganizer(models.Model):
    first_name = models.CharField(max_length =30)
    last_name = models.CharField(max_length =30)
    email = models.EmailField()
    

    def __str__(self):
        return self.first_name
    class meta:
        ordering =['name']
    
    def save_eventorganizer(self):
        self.save()


class tickets(models.Model):
    name = models.CharField(max_length =30)

    def __str__(self):
        return self.name

class Event(models.Model):
    title = models.CharField(max_length =60)
    post = HTMLField(default='')
    eventorganizer = models.ForeignKey(User,on_delete=models.CASCADE,default='')
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    tickets = models.ManyToManyField(tickets)
    pub_date = models.DateTimeField(auto_now_add=True)
    event_image = models.ImageField(upload_to = 'events/')

    def __str__(self):
        return self.title
    @classmethod
    def todays_event(cls):
        today = dt.date.today()
        event = cls.objects.filter(pub_date__date = today)
        return event
    
    @classmethod
    def days_event(cls,date):
        event = cls.objects.filter(pub_date__date = date)
        return event
    
    @classmethod
    def search_by_title(cls,search_term):
        event = cls.objects.filter(title__icontains=search_term)
        return event

class NewsLetterRecipients(models.Model):
    name = models.CharField(max_length = 30)
    email = models.EmailField()

class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    def save_category(self):
        self.save()

    def delete_category(self):
        self.delete()


