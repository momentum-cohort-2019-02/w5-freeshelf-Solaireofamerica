from django.shortcuts import render
from .models import Book
# Create your views here.

def home(request):
    return render(request, 'core/index.html', {'title': 'Home'})

# def book(request):
#     return render(request, 'core/books.html', {'title': ''})

def books(request):
    context = {
        'books': Book.objects.all()
    }
    return render(request, 'core/books.html', context)
