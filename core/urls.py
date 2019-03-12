from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='core-home'),
    path('books/', views.books, name='core-books')
]
