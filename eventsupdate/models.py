from django.db import models
import datetime as dt



# Create your models here.


class User(models.Model):
    first_name = models.CharField(max_length =30)
    last_name = models.CharField(max_length =30)
    email = models.EmailField()
    

    def __str__(self):
        return self.first_name
    class meta:
        ordering =['name']
    
    def save_user(self):
        self.save()

class Event(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    def save_category(self):
        self.save()

    def delete_category(self):
        self.delete()

