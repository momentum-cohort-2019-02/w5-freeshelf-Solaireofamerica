from django.db import models
from django.template.defaultfilters import slugify

# Create your models here.

class Author(models.Model):
    name = models.CharField(max_length=100, default="")
    # books_written = models.ManyToManyField('Book', help_text="Enter the info for all of the books this author has written.", blank=True)

    def __str__(self):
        return self.name

# class Language(models.Model):
#     lang = models.ManyToManyField('Book', help_text="Enter the programming language that this book pertains to.")


# need to add a slug field in the admin section
class Book(models.Model):
    title = models.CharField(max_length=100)
    author_of_book = models.ManyToManyField('Author', help_text="Enter the name of the person that wrote this book.", related_name="authors")
    description = models.TextField()
    added_on = models.DateTimeField(auto_now_add=True)
    # lang_of_book = models.CharField(empty_value, max_length=50)
    book_url = models.URLField(max_length=400, default="")
    slug = models.SlugField(default="")

    def __str__(self):
        return self.title
