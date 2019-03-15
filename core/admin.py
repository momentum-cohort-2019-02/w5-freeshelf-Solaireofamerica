from django.contrib import admin
from core.models import Author, Book, Categories
# Register your models here.

admin.site.register(Author)

# admin.site.register(Book)


@admin.register(Book)
class Book(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title", )}


@admin.register(Categories)
class Categories(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title", )}
