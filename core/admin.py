from django.contrib import admin
from core.models import Author, Book, Category
# Register your models here.

admin.site.register(Author)

# admin.site.register(Book)


@admin.register(Book)
class Book(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title", )}


@admin.register(Category)
class Category(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name", )}
