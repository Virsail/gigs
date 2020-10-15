from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm
from .models import User, Event, Category


# Create your views here.


def registerPage(request):
    form = UserCreationForm


    if request.method == 'POST':
         form = UserCreationForm(request.POST)
         if form.is_valid():
             form.save

    context = {'form':form}
    return render(request, 'accounts/register.html', context)


def loginPage(request):
    context = {}
    return render(request, 'accounts/login.html', context)