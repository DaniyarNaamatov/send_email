from django.db import models
from django.urls import reverse


class Contact(models.Model):
    username = models.CharField(max_length=150, verbose_name='Имя фамилия')
    phone = models.IntegerField(blank=True, verbose_name='Телефон')
    email = models.EmailField(blank=True, verbose_name='E-mail')
    descriptions = models.TextField(verbose_name='Описание')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Обновлено')

    def get_absolute_url(self):
        return reverse('request', kwargs={"pk": self.pk})

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = 'Контакт'
        verbose_name_plural = 'Контакты'
        ordering = ['-created_at']

