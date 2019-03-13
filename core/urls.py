from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='core-home'),
    path('books/', views.books, name='core-books'),
    path('book/<int:pk>', views.BookDetailView.as_view(), name='book_detail'),
]
