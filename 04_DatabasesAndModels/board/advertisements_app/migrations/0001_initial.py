# Generated by Django 4.1.2 on 2022-10-31 15:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AdvertisementCategories',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Host',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100, verbose_name='Имя владельца обьвления')),
                ('phone_number', models.CharField(max_length=12, verbose_name='мобильный телефон')),
                ('email', models.EmailField(max_length=254, verbose_name='почта')),
            ],
        ),
        migrations.CreateModel(
            name='Advertisement',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=1000, verbose_name='Загаловок')),
                ('options', models.CharField(max_length=1000, verbose_name='Описание')),
                ('created_at', models.DateField(auto_now_add=True)),
                ('public_end', models.DateField(verbose_name='окончание публикации')),
                ('updated_at', models.DateField(auto_now=True)),
                ('price', models.FloatField(default=0, verbose_name='price')),
                ('views_count', models.IntegerField(default=0, verbose_name='просмотры')),
                ('owner', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='advertisements_app.host')),
                ('status', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='advertisements_app.advertisementcategories')),
            ],
            options={
                'db_table': 'advertisements_app',
                'ordering': ['title'],
            },
        ),
    ]
