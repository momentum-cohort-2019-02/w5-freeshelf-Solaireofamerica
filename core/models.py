from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model

# Create your models here.

User = get_user_model()


class Author(models.Model):
    name = models.CharField(max_length=100, default="")

    def __str__(self):
        return self.name


# need to add a slug field to the site
class Book(models.Model):
    title = models.CharField(max_length=100)
    author_of_book = models.ManyToManyField(
        'Author',
        help_text="Enter the name of the person that wrote this book.",
        related_name="authors",
    )
    description = models.TextField()
    added_on = models.DateTimeField(auto_now_add=True)
    book_url = models.URLField(max_length=400, default="")
    slug = models.SlugField()

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-added_on']

    def get_absolute_url(self):
        return reverse("book_detail", args=(self.pk, ))


class Language(models.Model)