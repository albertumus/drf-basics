# Generated by Django 2.2.24 on 2021-11-03 09:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recetas', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='receta',
            name='imagen',
            field=models.ImageField(null=True, upload_to=''),
        ),
    ]
