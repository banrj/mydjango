# Generated by Django 4.1.3 on 2022-12-13 11:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_library', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=254)),
                ('biography', models.TextField()),
            ],
        ),
    ]
