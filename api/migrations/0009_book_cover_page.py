# Generated by Django 4.1.6 on 2023-02-17 08:10

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0008_remove_book_cover_page'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='cover_page',
            field=cloudinary.models.CloudinaryField(blank=True, max_length=255, null=True, verbose_name='image'),
        ),
    ]
