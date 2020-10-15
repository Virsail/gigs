from django.db import models
import datetime as dt
from pyuploadcare.dj.models import ImageField
from pyuploadcare.dj.forms import FileWidget


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
