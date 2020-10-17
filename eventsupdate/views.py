from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm
from .models import User

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages 


#Create your views here.


def registerPage(request):
     if request.user.is_authenticated:
         return redirect('index.html')
     else:
            form = CreateUserForm
     if request.method == 'POST':
                 form = UserCreationForm(request.POST)
     if form.is_valid():
        form.save
        user = form.cleaned_data.get('username')

        messages.success(request, 'Account has been created Successfully for ' + user)

        return redirect('login.html')

        context = {'form':form}
        return render(request, 'register.html', context)


def loginPage(request):
    if request.user.is_authenticated:
         return redirect('index.html')
    else:


        if request.method == 'POST':
                username = request.POST.get('username')
                password = request.POST.get('password')

                user = authenticate(request, username=username, password=password)

                if user is not None:
                        login(request, user)

                return redirect('index.html')

        else:
                messages.info(request, 'Username or password is incorrect')
                            
                context = {}
        return render(request, 'login.html', context)

def logoutUser(request):
    logout(request)
    return redirect('login.html')

@login_required(login_url='login.html')
def index(request):
      return render(request, 'index.html')












def search_results(request):
    if 'imagesearch' in request.GET and request.GET["imagesearch"]:
        category = request.GET.get("imagesearch")
        searched_images = Image.search_by_category(category)
        message = f"{category}"
        print(searched_images)
        return render(request, 'pictures/search_results.html', {"message": message, "images": searched_images})
    else:
        message = "You haven't searched for any image category"
        return render(request, 'pictures/search_results.html', {"message": message})


# Create your views here.
