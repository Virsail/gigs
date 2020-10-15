from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm


# Create your views here.
from .models import User, Event, Category


def registerPage(request):
    form = UserCreationForm
    context = {'form':form}
    return render(request)