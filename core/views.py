from django.shortcuts import render
from .models import Book, Category
from django.views import generic

# Create your views here.


def home(request):
    return render(request, 'core/index.html', {'title': 'Home'})


def books(request):
    context = {'books': Book.objects.all()}
    return render(request, 'core/books.html', context)


def categories(request):
    context = {'categories': Category.objects.all()}
    return render(request, 'category_detail.html', context)


# class CategoryView(generic.DetailView):
#     model = Category
#     fields = '__all__'


class BookDetailView(generic.DetailView):
    model = Book


class CategoryDetailView(generic.DetailView):
    model = Category