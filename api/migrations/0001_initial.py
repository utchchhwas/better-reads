# Generated by Django 4.1.6 on 2023-02-16 20:45

import api.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('image', models.ImageField(blank=True, default=None, null=True, upload_to=api.models.authorImagePath)),
            ],
            options={
                'verbose_name_plural': 'Authors',
            },
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('isbn', models.PositiveBigIntegerField(unique=True)),
                ('name', models.CharField(max_length=100)),
                ('edition', models.CharField(max_length=100)),
                ('publication_year', models.PositiveIntegerField()),
                ('language', models.CharField(max_length=100)),
                ('country', models.CharField(max_length=100)),
                ('number_of_pages', models.PositiveIntegerField()),
                ('cover_page', models.ImageField(blank=True, default=None, null=True, upload_to=api.models.bookCoverImagePath)),
            ],
            options={
                'verbose_name_plural': 'Books',
            },
        ),
        migrations.CreateModel(
            name='Publisher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name_plural': 'Publishers',
            },
        ),
        migrations.CreateModel(
            name='BookCatagory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('catagory', models.CharField(max_length=100)),
                ('parent', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='api.bookcatagory')),
            ],
            options={
                'verbose_name_plural': 'Book Catagories',
            },
        ),
        migrations.CreateModel(
            name='BookAuthor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rank', models.IntegerField()),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.author')),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.book')),
            ],
            options={
                'verbose_name_plural': 'Book Authors',
            },
        ),
        migrations.AddField(
            model_name='book',
            name='authors',
            field=models.ManyToManyField(through='api.BookAuthor', to='api.author'),
        ),
        migrations.AddField(
            model_name='book',
            name='catagories',
            field=models.ManyToManyField(to='api.bookcatagory'),
        ),
        migrations.AddField(
            model_name='book',
            name='publisher',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.publisher'),
        ),
        migrations.AddConstraint(
            model_name='bookauthor',
            constraint=models.UniqueConstraint(fields=('book', 'author'), name='unique book author'),
        ),
        migrations.AddConstraint(
            model_name='bookauthor',
            constraint=models.UniqueConstraint(fields=('book', 'rank'), name='unique book rank'),
        ),
    ]
