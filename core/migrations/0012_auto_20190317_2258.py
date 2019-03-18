# Generated by Django 2.1.7 on 2019-03-18 03:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0011_auto_20190315_1438'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=50)),
                ('name', models.CharField(max_length=50)),
                ('slug', models.SlugField()),
            ],
        ),
        migrations.RemoveField(
            model_name='book',
            name='category',
        ),
        migrations.DeleteModel(
            name='Categories',
        ),
        migrations.AddField(
            model_name='book',
            name='categories',
            field=models.ManyToManyField(help_text='Enter the Category/s for the book.', related_name='category', to='core.Category'),
        ),
    ]