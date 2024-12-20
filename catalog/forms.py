from django import forms
from datetime import date
from django.forms import ModelForm
from .models import Book
from .models import Person
from .models import Image
from .models import File
from .models import VideoFile
from .models import AudioFile 
from .models import Author

class AuthorsForm(forms.Form):
 first_name = forms.CharField(label="Имя автора")
 last_name = forms.CharField(label="Фамилия автора")
 date_of_birth = forms.DateField(label="Дата рождения",
        initial=format(date.today()),
        widget=forms.widgets.DateInput(attrs={'type': 'date'}))
 date_of_death = forms.DateField(label="Дата смерти",
        initial=format(date.today()),
        widget=forms.widgets.DateInput(attrs={'type': 'date'}))

class Form_add_author(forms.Form):
 first_name = forms.CharField(label="Имя автора")
 last_name = forms.CharField(label="Фамилия автора")
 date_of_birth = forms.DateField(
 label="Дата рождения",
 initial=format(date.today()),
 widget=forms.widgets.DateInput(attrs={'type': 'date'}))
 about = forms.CharField(label="Сведения об авторе",
 widget=forms.Textarea)
 photo = forms.ImageField(label="Фото автора")

class Form_edit_author(forms.ModelForm):
 class Meta:
  model = Author
  fields = '__all__'
 
class BookModelForm(ModelForm):
 class Meta:
  model = Book
  fields = '__all__'

class UserForm(ModelForm):
   class Meta:
     model = Person
     fields = ['name','age']

class ImageForm(forms.ModelForm):
 class Meta:
  model = Image
  fields = '__all__'
  #fields = ['title', 'image']

class FileForm(forms.ModelForm):
 class Meta:
  model = File
  fields = '__all__'

class VideoForm(forms.ModelForm):
 class Meta:
  model = VideoFile
  fields = '__all__'

class AudioForm(forms.ModelForm):
 class Meta:
  model = AudioFile
  fields = '__all__'
