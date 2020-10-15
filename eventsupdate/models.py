from django.db import models
import datetime as dt
from pyuploadcare.dj.models import ImageField
from pyuploadcare.dj.forms import FileWidget


# Create your models here.


class Editor(models.Model):
    first_name = models.CharField(max_length =30)
    last_name = models.CharField(max_length =30)
    email = models.EmailField()
    phone_number = models.CharField(max_length = 10,blank =True)

    def __str__(self):
        return self.first_name
    class meta:
        ordering =['name']
    
    def save_editor(self):
        self.save()
