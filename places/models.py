from django.db import models
from tinymce.models import HTMLField


class Excursion(models.Model):
    title = models.CharField(max_length=200, verbose_name='Название экскурсии')
    short_description = models.TextField(blank=True, verbose_name='Короткое описание')
    long_description = HTMLField(blank=True, verbose_name='Длинное описание')
    lat = models.FloatField(verbose_name='Широта')
    lon = models.FloatField(verbose_name='Долгота')

    def __str__(self):
        return self.title


class Image(models.Model):
    excursion_title = models.ForeignKey(Excursion, on_delete=models.CASCADE, verbose_name='Название экскурсии')
    image = models.ImageField(upload_to='', verbose_name='Название картинки')
    position = models.PositiveIntegerField(default=0, verbose_name='Позиция', db_index=True)

    class Meta:
        ordering = ['position']

    def __str__(self):
        return self.excursion_title
