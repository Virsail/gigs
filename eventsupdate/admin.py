from django.contrib import admin
from .models import EventOrganizer,Event,tickets,Category
# Register your models here.
admin.site.register(EventOrganizer)
admin.site.register(Event)
admin.site.register(tickets)
admin.site.register(Category)