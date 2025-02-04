from django.db import models

class Buyer(models.Model):
    name = models.CharField(max_length=255,verbose_name="Имя покупателя")  # Имя покупателя
    balance = models.DecimalField(max_digits=10, decimal_places=2, default=0.00, verbose_name="Баланс")  # Баланс покупателя
    age = models.IntegerField(verbose_name="Возраст")  # Возраст покупателя

    def __str__(self):
        return self.name


class Game(models.Model):
    title = models.CharField(max_length=255,verbose_name="Название игры")  # Название игры
    cost = models.DecimalField(max_digits=10, decimal_places=2,verbose_name="Цена")  # Цена игры
    size = models.DecimalField(max_digits=10, decimal_places=2,verbose_name="Размер (ГБ)")  # Размер файлов игры
    description = models.TextField(verbose_name="Описание игры")  # Описание игры
    age_limited = models.BooleanField(default=False, verbose_name="Ограничение по возрасту")  # Ограничение по возрасту
    buyer = models.ManyToManyField(Buyer, related_name='games',verbose_name="Покупатели")  # Связь с покупателями

    def __str__(self):
        return self.title



class Meta:
    verbose_name = "Покупатель"
    verbose_name_plural = "Покупатели"


