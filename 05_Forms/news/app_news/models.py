from django.db import models


class News(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200, verbose_name='Загаловок')
    options = models.TextField(max_length=1000, verbose_name='Описание')
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    flag = models.CharField(max_length=20,  choices=(('Active', 'Активно'), ('Deactive', 'Неактивно')))

    class Meta:
        db_table = 'News'
        ordering = ['created_at']


class Comments(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=40, verbose_name='Имя пользователя')
    text = models.TextField(max_length=1000, verbose_name='Текст')
    news = models.ForeignKey(News, on_delete=models.CASCADE, related_name='comment_news')
    created_at = models.DateField(auto_now_add=True)

    class Meta:
        db_table = 'Comments'
        ordering = ['created_at']
