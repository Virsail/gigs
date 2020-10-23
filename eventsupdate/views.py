from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404,HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm
from .forms import SignUpForm
from .models import Event, NewsLetterRecipients
import datetime as dt
from .email import send_welcome_email
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages 
from django.http import JsonResponse
from .forms import EventLetterForm, NewEventForm






#Create your views here.


def registerPage(request):
     if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            messages.success(request, 'Account has been created Successfully for ' + user)
            return redirect('today-events.html')
     else:
        form = SignUpForm()
        return render(request, 'registration/registration_form.html', {'form': form})


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

                #return redirect('index.html')

        else:
                messages.info(request, 'Username or password is incorrect')
                            
                context = {}
        return render(request, 'login.html', context)

def logoutUser(request):
    logout(request)
    return render(request, 'login.html')

  

#@login_required(login_url='/accounts/login/')
def index(request):
      return render(request, 'index.html')



def event_today(request):
    date = dt.date.today()
    events = Event.todays_event()
    if request.method == 'POST':
         form = EventLetterForm(request.POST)
         if form.is_valid():
              print('valid')
              name = form.cleaned_data['your_name']
              email = form.cleaned_data['email']
              recipient = NewsLetterRecipients(name = name,email =email)
              recipient.save()
              send_welcome_email(name,email)


    #          HttpResponseRedirect('event_today')
    # else:
    form = EventLetterForm()
    return render(request, 'all-events/today-events.html',{'date': date,"events":events,"letterForm":form})

def eventletter(request):
    name = request.POST.get('your_name')
    email = request.POST.get('email')

    recipient = NewsLetterRecipients(name=name, email=email)
    recipient.save()
    send_welcome_email(name, email)
    data = {'success': 'Welcome to Events Pub !You have been successfully added to mailing list'}
    return JsonResponse(data)

def show_events(request,past_date):
    
    try:
        # Converts data from the string Url
        date = dt.datetime.strptime(past_date,'%Y-%m-%d').date()
    except ValueError:
        # Raise 404 error when ValueError is thrown
        raise Http404()
        assert False

    if date == dt.date.today():
        return redirect(events_today)
    
    event = Event.days_event(date)
    return render(request, 'all-events/show-events.html', {"date":date,"event":event})

def search_results(request):
    
    if 'event' in request.GET and request.GET["event"]:
        search_term = request.GET.get("event")
        searched_events = Event.search_by_title(search_term)
        message = f"{search_term}"

        return render(request, 'all-events/search.html',{"message":message,"events": searched_events})

    else:
     message = "Stay home and remember to sanitize"
     return render(request, 'all-events/search.html',{"message":message})

@login_required(login_url='/accounts/login/')    
def event(request,event_id):
    try:
        event = Event.objects.get(id = event_id)
    except DoesNotExist:
        raise Http404()
    return render(request,"all-events/event.html", {"event":event})

@login_required(login_url='/accounts/login/')
def new_event(request):
    current_user = request.user
    if request.method == 'POST':
        form = NewEventForm(request.POST, request.FILES)
        if form.is_valid():
            event = form.save(commit=False)
            event.editor = current_user
            event.save()
        return redirect('eventsToday')
    else:
        form = NewEventForm()
    return render(request, 'new_event.html', {"form": form})







