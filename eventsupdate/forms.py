from django.forms import ModelForm
from .models import Event 
from django.contrib.auth.forms import UserCreationForm
from django.contrib .auth.models import User
from django import forms
#from .models import Article
class EventForm(ModelForm):
     class Meta:
         model = Event
         fields = '__all__'






class CreateUserForm( UserCreationForm):
     class Meta:
         model = User
         fields = ['username', 'email', 'password1', 'password2' ]




class NewsLetterForm(forms.Form):
    your_name = forms.CharField(label='First Name',max_length=30)
    email = forms.EmailField(label='Email')

#class NewArticleForm(forms.ModelForm):
#    class Meta:
#        model = Article
#        exclude = ['editor', 'pub_date']
#        widgets = {
#            'tags': forms.CheckboxSelectMultiple(),
#        }


