# Generated by Django 4.0.1 on 2022-02-10 22:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BlogApp', '0003_alter_bio_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bio',
            name='biografia',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='blog',
            name='contenido',
            field=models.TextField(),
        ),
    ]
