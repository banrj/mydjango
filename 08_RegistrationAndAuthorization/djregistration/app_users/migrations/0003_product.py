# Generated by Django 2.2 on 2023-02-22 23:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app_users', '0002_auto_20230222_2225'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.IntegerField()),
                ('product_name', models.CharField(max_length=25, verbose_name='Название')),
                ('options', models.TextField(max_length=100, null=True, verbose_name='Описание')),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='creater', to='app_users.Profile')),
            ],
            options={
                'db_table': 'Products',
                'ordering': ['created_by', 'id'],
            },
        ),
    ]
