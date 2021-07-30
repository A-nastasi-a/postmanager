from django.db import models
import django.db.models

# Create your models here.
class Orders(models.Model):
    title = models.CharField('Название', max_length=50)
    sender_name = models.CharField('Имя отправителя', max_length=50)
    sender_addres = models.TextField('Адрес отправителя')
    receiver_name = models.CharField('Имя получателя', max_length=50)
    receiver_addres = models.TextField('Адрес получателя')
    date_of_creating = models.DateTimeField('Дата создания', auto_now=True)
    weight = models.IntegerField('Вес посылки, г.')

    def __str__(self):
        return {self.title}

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'