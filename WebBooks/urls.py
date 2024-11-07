"""
URL configuration for WebBooks project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path, include
from catalog import views

urlpatterns = [
 path('', views.index, name='index'),
 path('admin/', admin.site.urls),
 path('accounts/', include('django.contrib.auth.urls')),
 re_path(r'^books/$', views.BookListView.as_view(), name='books'),
 re_path(r'^book/(?P<pk>\d+)$', views.BookDetailView.as_view(), name='book-detail'),
 re_path(r'^authors/$', views.AuthorListView.as_view(), name='authors'),
 path('mybooks/', views.LoanedBooksByUserListView.as_view(), name='my-borrowed'),
 path('authors_add/', views.authors_add, name='authors_add'),
 path('edit1/<int:id>/', views.edit1, name='edit1'),
 path('create/', views.create, name='create'),
 path('delete/<int:id>/', views.delete, name='delete'),
 re_path(r'^book/create/$', views.BookCreate.as_view(), name='book_create'),
 re_path(r'^book/update/(?P<pk>\d+)$', views.BookUpdate.as_view(), name='book_update'),
 re_path(r'^book/delete/(?P<pk>\d+)$', views.BookDelete.as_view(), name='book_delete'),
 path('start1/', views.start1, name='start1'),
 path('color_bg/', views.color_bg, name='color-bg'),
 path('color_text/', views.color_text, name='color_text'),
 path('color_text_bg/', views.color_text_bg, name='color_text_bg'),
 path('space_1/', views.space_1, name='space_1'),
 path('space_2/', views.space_2, name='space_2'),
 path('space_3/', views.space_3, name='space_3'),
 path('aligment_1/', views.aligment_1, name='aligment_1'),
 path('aligment_2/', views.aligment_2, name='aligment_2'),
 path('border_1/', views.border_1, name='border_1'),
 path('border_2/', views.border_2, name='border_2'),
 path('border_color/', views.border_color, name='border_color'),
 path('border_radius/', views.border_radius, name='border_radius'),
 path('border_radius_1/', views.border_radius_1, name='border_radius_1'),
 path('start/', views.start, name='start'),
 path('table/', views.table, name='table'),
 path('table_1/', views.table_1, name='table_1'),
 path('', views.index, name='index'),
 path('about/', views.about, name='about'),
 path('contact/', views.contact, name='contact'),
 path('my_form/', views.my_form,name='my_form'),
]
