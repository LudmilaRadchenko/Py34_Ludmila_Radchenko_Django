# Generated by Django 4.1.5 on 2023-01-24 13:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='book_cover',
            field=models.ImageField(blank=True, upload_to='authors/'),
        ),
        migrations.AddField(
            model_name='genre',
            name='genre_picture',
            field=models.ImageField(blank=True, upload_to='authors/'),
        ),
    ]
