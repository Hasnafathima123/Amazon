# Generated by Django 4.1.4 on 2023-09-22 07:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shops',
            name='image',
            field=models.TextField(max_length=500),
        ),
    ]
