from django.shortcuts import render
from .models import Book, Categories
from django.views import generic

# Create your views here.


def home(request):
    return render(request, 'core/index.html', {'title': 'Home'})


# def book(request):
#     return render(request, 'core/books.html', {'title': ''})


def books(request):
    context = {'books': Book.objects.all()}
    return render(request, 'core/books.html', context)


# def book_detail_view(request, slug):
#     book = get_object_or_404(Book, slug=slug)
#     return render(
#         request,
#         "core/book_detail.html",
#         {"book": book},
#     )


class CategoryView(generic.DetailView):
    model = Categories


class BookDetailView(generic.DetailView):
    model = Book
