# Generated by Django 2.1.7 on 2019-03-11 18:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20190311_1337'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='language',
            name='lang',
        ),
        migrations.RemoveField(
            model_name='book',
            name='language_of_book',
        ),
        migrations.AlterField(
            model_name='author',
            name='books_written',
            field=models.ManyToManyField(blank=True, help_text='Enter the info for all of the books this author has written.', to='core.Book'),
        ),
        migrations.DeleteModel(
            name='Language',
        ),
    ]
