# Generated by Django 4.1.5 on 2023-01-31 17:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0003_alter_book_book_cover_alter_genre_genre_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='book_cover',
            field=models.ImageField(blank=True, default='book-placeholder.jpg', upload_to='books/'),
        ),
    ]