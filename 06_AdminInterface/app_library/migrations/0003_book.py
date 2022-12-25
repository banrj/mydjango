# Generated by Django 4.1.3 on 2022-12-18 11:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app_library', '0002_author'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('publication_date', models.DateField()),
                ('authors', models.ManyToManyField(to='app_library.author')),
                ('publisher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_library.publisher')),
            ],
        ),
    ]
