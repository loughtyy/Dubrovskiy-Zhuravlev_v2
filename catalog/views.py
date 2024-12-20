from .models import Book, Author, BookInstance, Genre
from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views import generic
from .forms import Form_add_author
from .forms import Form_edit_author
from .forms import AuthorsForm
from .models import Book
from .forms import UserForm
from .forms import ImageForm
from .models import Person
from .models import Image
from django.shortcuts import redirect
from django.http import *
from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import File
from .forms import FileForm
from .models import VideoFile
from .forms import VideoForm
from .models import AudioFile
from .forms import AudioForm



def index(request):
 text_head = 'На нашем сайте вы можете получить книги в электронном виде'
 books = Book.objects.all()
 num_books = Book.objects.all().count()
 num_instances = BookInstance.objects.all().count()
 num_instances_available = BookInstance.objects.filter(
 status__exact=2).count()
 authors = Author.objects
 num_authors = Author.objects.count()
 num_visits = request.session.get('num_visits', 0)
 request.session['num_visits'] = num_visits + 1
 context = {'text_head': text_head,
  'books': books, 'num_books': num_books,
  'num_instances': num_instances,
  'num_instances_available': num_instances_available,
  'authors': authors, 'num_authors': num_authors,
  'num_visits': num_visits}
 return render(request, 'index.html', context)
class BookListView(generic.ListView):
 model = Book
 context_object_name = 'books'
 paginate_by = 3


class BookDetailView(generic.DetailView):
    model = Book
    context_object_name = 'book'

class AuthorListView(generic.ListView):
    model = Author
    paginate_by = 4

class AuthorDetailView(generic.DetailView):
 model = Author

class BookCreate(CreateView):
 model = Book
 fields = '__all__'
 success_url = reverse_lazy('edit_books')

class BookUpdate(UpdateView):
 model = Book
 fields = '__all__'
 success_url = reverse_lazy('edit_books')

class BookDelete(DeleteView):
 model = Book
 success_url = reverse_lazy('edit_books')

from django.contrib.auth.mixins import LoginRequiredMixin
class LoanedBooksByUserListView(LoginRequiredMixin, generic.ListView):
 model = BookInstance
 template_name = 'catalog/Bookinstance_list_Borrowed_user.html'
 paginate_by = 10
 def get_queryset(self):
    return BookInstance.objects.filter(borrower=self.request.user).filter(status__exact='2').order_by('due_back')
 

def edit_authors(request):
 author = Author.objects.all()
 context = {'author': author}
 return render(request, "catalog/edit_authors.html", context)

def create(request):
 if request.method == "POST":
  author = Author()
  author.first_name = request.POST.get("first_name")
  author.last_name = request.POST.get("last_name")
  author.date_of_birth = request.POST.get("date_of_birth")
  author.date_of_death = request.POST.get("date_of_death")
  author.save()
  return HttpResponseRedirect("/edit_authors/")

def delete(request, id):
 try:
  author = Author.objects.get(id=id)
  author.delete()
  return HttpResponseRedirect("/edit_authors/")
 except Author.DoesNotExist:
  return HttpResponseNotFound("<h2>Автор не найден</h2>")

def edit1(request, id):
 author = Author.objects.get(id=id)
 if request.method == "POST":
   author.first_name = request.POST.get("first_name")
   author.last_name = request.POST.get("last_name")
   author.date_of_birth = request.POST.get("date_of_birth")
   author.date_of_death = request.POST.get("date_of_death")
   author.save()
   return HttpResponseRedirect("/authors_add/")
 else:
  return render(request, "edit1.html", {"author": author})
 
class BookCreate(CreateView):
 model = Book
 fields = '__all__'
 success_url = reverse_lazy('books')
class BookUpdate(UpdateView):
 model = Book
 fields = '__all__'
 success_url = reverse_lazy('books')
class BookDelete(DeleteView):
 model = Book
 success_url = reverse_lazy('books')

def about(request):
 text_head = 'Сведения о компании'
 name = 'ООО "Интеллектуальные информационные системы"'
 rab1 = 'Разработка приложений на основе' \
 ' систем искусственного интеллекта'
 rab2 = 'Распознавание объектов дорожной инфраструктуры'
 rab3 = 'Создание графических АРТ-объектов на основе' \
 ' систем искусственного интеллекта'
 rab4 = 'Создание цифровых интерактивных книг, учебных пособий' \
 ' автоматизированных обучающих систем'
 context = {'text_head': text_head, 'name': name,
 'rab1': rab1, 'rab2': rab2,
 'rab3': rab3, 'rab4': rab4}
 return render(request, 'catalog/about.html', context)

def contact(request):
 text_head = 'Контакты'
 name = 'ООО "Интеллектуальные информационные системы"'
 address = 'Москва, ул. Планерная, д.20, к.1'
 tel = '495-345-45-45'
 email = 'iis_info@mail.ru'
 context = {'text_head': text_head,
 'name': name, 'address': address,
 'tel': tel,
 'email': email}
 return render(request, 'catalog/contact.html', context)

class LoanedBooksByUserListView(LoginRequiredMixin, generic.ListView):
 model = BookInstance
 template_name = 'catalog/bookinstance_list_borrowed_user.html'
 paginate_by = 10
 def get_queryset(self):
  return BookInstance.objects.filter(
 borrower=self.request.user).filter(
 status__exact='2').order_by('due_back')


def add_author(request):
 if request.method == 'POST':
  form = Form_add_author(request.POST, request.FILES)
  if form.is_valid():
   first_name = form.cleaned_data.get("first_name")
   last_name = form.cleaned_data.get("last_name")
   date_of_birth = form.cleaned_data.get("date_of_birth")
   about = form.cleaned_data.get("about")
   photo = form.cleaned_data.get("photo")
   obj = Author.objects.create(
    first_name=first_name,
    last_name=last_name,
    date_of_birth=date_of_birth,
    about=about,
    photo=photo)
   obj.save()
   return HttpResponseRedirect(reverse('authors'))
 else:
  form = Form_add_author()
  context = {"form": form}
  return render(request, "catalog/authors_add.html", context)

def edit_author(request, id):
 author = Author.objects.get(id=id)
 # author = get_object_or_404(Author, pk=id)
 if request.method == "POST":
  instance = Author.objects.get(pk=id)
  form = Form_edit_author(request.POST, request.FILES, instance=instance)
  if form.is_valid():
   form.save()
   return HttpResponseRedirect("/edit_authors/")
 else:
  form = Form_edit_author(instance=author)
  content = {"form": form}
  return render(request, "catalog/edit_author.html", content)

def edit_books(request):
 book = Book.objects.all()
 context = {'book': book}
 return render(request, "catalog/edit_books.html", context)

# def start1(request):
#     return render(request, "boob/start1.html")
# def color_bg(request):
#     return render(request,"boob/color_bg.html")
# def color_text(request):
#     return render(request,'boob/color_text.html')
# def color_text_bg(request):
#     return render(request, 'boob/color_text_bg.html')
# def space_1(request):
#   return render(request, 'boob/space_1.html')
# def space_2(request):
#   return render(request, 'boob/space_2.html')
# def space_3(request):
#   return render(request, 'boob/space_3.html')
# def aligment_1(request):
#   return render(request, 'boob/aligment_1.html')
# def aligment_2(request):
#   return render(request, 'boob/aligment_2.html')
# def border_1(request):
#   return render(request, 'boob/border_1.html')
# def border_2(request):
#   return render(request, 'boob/border_2.html')
# def border_color(request):
#   return render(request, 'boob/border_color.html')
# def border_radius(request):
#   return render(request, 'boob/border_radius.html')
# def border_radius_1(request):
#   return render(request, 'boob/border_radius_1.html')
# def start(request):
#     return render(request, "boob/start.html")
# def table(request):
#     return render(request, "boob/table.html")
# def table_1(request):
#     return render(request, "boob/table_1.html")
# def index(request):
#  return render(request, "app/index.html")

# def index(request):
#  return render(request, "app/index.html")
# def about(request):
#  return render(request, "app/about.html")
# def contact(request):
#  return render(request, "app/contact.html")
# def index(request):
#  my_kv = ['I квартал ->', 'II квартал ->', 'III квартал->',
#  'IV квартал->']
#  my_month = ['Январь', 'Февраль', 'Март',
#  'Апрель', 'Май', 'Июнь',
#  'Июль', 'Август', 'Сентябрь',
#  'Октябрь', 'Ноябрь', 'Декабрь']
#  context = {'my_month': my_month, 'my_kv': my_kv}
#  return render(request, "app/index.html", context)



# def index(request):
#  my_text = 'Изучаем формы Django'
#  people_kol = Person.object_person.count()
#  context = {'my_text': my_text,"people_kol": people_kol}
#  return render(request, "app/index.html", context)
# def about(request):
#  return render(request, "app/about.html")
# def contact(request):
#  return render(request, "app/contact.html")


# def my_form(request):
#  if request.method == "POST": 
#   form = UserForm(request.POST) 
#   if form.is_valid(): 
#     form.save()
#  my_text = 'Сведения о клиентах'
#  people = Person.object_person.all()
#  form = UserForm()
#  context = {'my_text': my_text, "people": people, "form": form}
#  return render(request, "my_form.html", context)

# def edit_form(request, id):
#  person = Person.object_person.get(id=id)
#  if request.method == "POST":
#   person.name = request.POST.get("name")
#   person.age = request.POST.get("age")
#   person.save()
#   return redirect('my_form')
#  data = {"person": person}
#  return render(request, "edit_form.html", context=data)
# def delete(request, id):
#  try:
#   person = Person.object_person.get(id=id)
#   person.delete()
#   return redirect('my_form')
#  except Person.DoesNotExist:
#   return HttpResponseNotFound("<h2>Объект не найден</h2>")

# def form_up_img(request):
#  if request.method == 'POST':
#   form = ImageForm(request.POST, request.FILES)
#   if form.is_valid():
#    form.save()
#  my_text = 'Загруженные изображения'
#  my_img = Image.obj_img.all()
#  form = ImageForm()
#  context = {'my_text': my_text, "my_img": my_img, "form": form}
#  return render(request, 'app/form_up_img.html', context)

# def delete_img(request, id):
#  try:
#   img = Image.obj_img.get(id=id)
#   img.delete()
#   return redirect('form_up_img')
#  except Person.DoesNotExist:
#   return HttpResponseNotFound("<h2>Объект не найден</h2>")
 

# def form_up_pdf(request):
#  if request.method == 'POST':
#   form = FileForm(request.POST, request.FILES)
#   if form.is_valid():
#    form.save()
#  my_text = 'Загруженные файлы'
#  form = FileForm()
#  file_obj = File.objects.all()
#  context = {'my_text': my_text, "file_obj": file_obj, "form": form}
#  return render(request, 'app/form_up_pdf.html', context)
# def delete_pdf(request, id):
#  try:
#   pdf = File.objects.get(id=id)
#   pdf.delete()
#   return redirect('form_up_pdf')
#  except Person.DoesNotExist:
#   return HttpResponseNotFound("<h2>Объект не найден</h2>")
 

# def form_up_video(request):
#  if request.method == 'POST':
#   form = VideoForm(request.POST, request.FILES)
#   if form.is_valid():
#    form.save()
#  my_text = 'Загруженные видео файлы'
#  form = VideoForm()
#  file_obj = VideoFile.obj_video.all()
#  context = {'my_text': my_text, "file_obj": file_obj, "form": form}
#  return render(request, 'app/form_up_video.html', context)
# def delete_video(request, id):
#  try:
#   video = VideoFile.obj_video.get(id=id)
#   video.delete()
#   return redirect('form_up_video')
#  except Person.DoesNotExist:
#   return HttpResponseNotFound("<h2>Объект не найден</h2>")
 
# def form_up_audio(request):
#  if request.method == 'POST':
#   form = AudioForm(request.POST, request.FILES)
#   if form.is_valid():
#    form.save()
#  my_text = 'Загруженные аудио файлы'
#  form = AudioForm()
#  file_obj = AudioFile.obj_audio.all()
#  context = {'my_text': my_text, "file_obj": file_obj, "form": form}
#  return render(request, 'app/form_up_audio.html', context)
# def delete_audio(request, id):
#  try:
#   audio = AudioFile.obj_audio.get(id=id)
#   audio.delete()
#   return redirect('form_up_audio')
#  except Person.DoesNotExist:
#   return HttpResponseNotFound("<h2>Объект не найден</h2>")