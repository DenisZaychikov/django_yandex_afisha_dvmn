from django.db import models
from tinymce.models import HTMLField


class Excursion(models.Model):
    title = models.CharField(max_length=200, verbose_name='Название экскурсии')
    description_short = models.TextField(blank=True, null=True, verbose_name='Короткое описание')
    description_long = HTMLField(blank=True, null=True, verbose_name='Длинное описание')
    lat = models.FloatField(blank=True, null=True, verbose_name='Широта')
    lon = models.FloatField(blank=True, null=True, verbose_name='Долгота')

    def __str__(self):
        return self.title


class Image(models.Model):
    excursion_title = models.ForeignKey(Excursion, on_delete=models.CASCADE, null=True, blank=True)
    image = models.ImageField(upload_to='', blank=True, null=True, verbose_name='Название картинки')
    position = models.PositiveIntegerField(default=0, verbose_name='Позиция')

    class Meta:
        ordering = ['position']

    def __str__(self):
        return f'{self.position} {self.excursion_title}'
