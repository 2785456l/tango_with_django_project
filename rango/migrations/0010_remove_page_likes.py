# Generated by Django 2.2.26 on 2023-02-03 01:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rango', '0009_page_likes'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='page',
            name='likes',
        ),
    ]
