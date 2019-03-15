from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model

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
    category = models.ManyToManyField(
        'Categories',
        help_text="Enter the Category/s for the book.",
        related_name="category",
    )

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-added_on']

    def get_absolute_url(self):
        return reverse("book_detail", args=(self.pk, ))


class Categories(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("(self)", args={self.slug})
