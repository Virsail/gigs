from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm
from .models import User, Event, Category

from django.contrib.auth import authenticate, login, logout

from django.contrib import messages 


# Create your views here.


def registerPage(request):
    form = CreateUserForm


    if request.method == 'POST':
         form = UserCreationForm(request.POST)
         if form.is_valid():
             form.save
             user = form.cleaned_data.get('username')

             messages.success(request, 'Account has been created Successfully for ' + )

             return redirect('login')

    context = {'form':form}
    return render(request, 'accounts/register.html', context)


def loginPage(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user = not None:
            login(request, user)

            return redirect('index')

            else:
                messages.info(request, 'Username or password is incorrect')


    context = {}
    return render(request, 'accounts/login.html', context)