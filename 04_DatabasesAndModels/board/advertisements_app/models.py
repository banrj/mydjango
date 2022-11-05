from django.db import models


class Advertisement(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=1000, verbose_name='Загаловок')
    options = models.CharField(max_length=1000, verbose_name='Описание')
    created_at = models.DateField(auto_now_add=True)
    public_end = models.DateField(verbose_name='окончание публикации')
    updated_at = models.DateField(auto_now=True)
    price = models.FloatField(verbose_name='price', default=0)
    views_count = models.IntegerField(verbose_name='просмотры', default=0)
    status = models.ForeignKey('AdvertisementCategories', default=None, null=True, on_delete=models.CASCADE)
    owner = models.ForeignKey('Host', default=None, on_delete=models.CASCADE, null=True, )

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'advertisement'
        ordering = ['title']


class AdvertisementCategories(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Host(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, verbose_name='Имя владельца обьвления')
    phone_number = models.CharField(max_length=12, verbose_name='мобильный телефон')
    email = models.EmailField(max_length=254, verbose_name='почта')

    def __str__(self):
        return self.name
