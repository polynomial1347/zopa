from django.db import models

class Task(models.Model):
    title = models.CharField('Имячко', max_length=100)
    task = models.TextField('Описание')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Проститутка'
        verbose_name_plural = 'Проститутки'