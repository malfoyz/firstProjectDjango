from tabnanny import verbose
from unittest.util import _MAX_LENGTH
from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _


class Section(models.Model):
    """Модель раздела"""

    title = models.CharField(
        max_length=64,
        verbose_name=_('Название'),
    )
    description = models.TextField(
        verbose_name=_('Описание'),
    )

    class Meta:
        verbose_name = _('Раздел')
        verbose_name_plural = _('Разделы')

    def get_absolute_url(self) -> str:
        return reverse('autoservice:section', args=(self.pk, ))
    
    def __str__(self) -> str:
        return self.title

class Service(models.Model):
    """Модель услуги"""

    image = models.ImageField(
        upload_to='services',
        verbose_name=_('Изображение'),
    )
    title = models.CharField(
        max_length=64,
        verbose_name=_('Название'),
    )
    description = models.TextField(
        verbose_name=_('Описание'),
    )
    price = models.DecimalField(
        max_digits=13,
        decimal_places=5,
        verbose_name=_('Цена (от)'),
    )
    section = models.ForeignKey(
        to=Section,
        on_delete=models.CASCADE,
        related_name='services',
        related_query_name='service',
    )

    class Meta:
        verbose_name = _('Услуга')
        verbose_name_plural = _('Услуги')

    def __str__(self) -> str:
        return self.title