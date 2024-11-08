from django import forms
from datetime import date
from django.forms import ModelForm
from .models import Book
from .models import Person
from .models import Image

class AuthorsForm(forms.Form):
 first_name = forms.CharField(label="Имя автора")
 last_name = forms.CharField(label="Фамилия автора")
 date_of_birth = forms.DateField(label="Дата рождения",
        initial=format(date.today()),
        widget=forms.widgets.DateInput(attrs={'type': 'date'}))
 date_of_death = forms.DateField(label="Дата смерти",
        initial=format(date.today()),
        widget=forms.widgets.DateInput(attrs={'type': 'date'}))
 
class BookModelForm(ModelForm):
 class Meta:
  model = Book
  fields = ['title', 'genre', 'language', 'author', 'summary', 'isbn']

class UserForm(ModelForm):
   class Meta:
     model = Person
     fields = ['name','age']

class ImageForm(forms.ModelForm):
 class Meta:
  model = Image
  fields = '__all__'
  #fields = ['title', 'image']
