# Generated by Django 5.2 on 2025-04-09 02:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_first_app', '0004_author_book_author'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='author',
            new_name='authors',
        ),
        migrations.AddField(
            model_name='author',
            name='birth_date',
            field=models.DateField(default='2000-01-01'),
            preserve_default=False,
        ),
    ]
