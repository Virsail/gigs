from django.forms import ModelForm
from .models import Event 
from django.contrib.auth.forms import UserCreationForm
from django.contrib .auth.models import User
from django import forms


#class EventForm(ModelForm):
#     class Meta:
#         model = Event
#         fields = '__all__'


class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')




#class CreateUserForm( UserCreationForm):
#     class Meta:
#         model = User
#         fields = ['username', 'email', 'password1', 'password2' ]




class EventLetterForm(forms.Form):
    your_name = forms.CharField(label='First Name',max_length=30)
    email = forms.EmailField(label='Email')

class NewEventForm(forms.ModelForm):
    class Meta:
        model = Event
        exclude = ['EventOrganizer', 'pub_date']
        widgets = {
            'tickets': forms.CheckboxSelectMultiple(),
        }


