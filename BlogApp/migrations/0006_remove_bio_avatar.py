# Generated by Django 4.0.1 on 2022-02-11 22:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('BlogApp', '0005_rename_imagen_bio_avatar'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bio',
            name='avatar',
        ),
    ]
