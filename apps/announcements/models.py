from django.db import models
from django.conf import settings


class Announcement(models.Model):
    title = models.CharField('Заголовок', max_length=180)
    content = models.TextField('Текст оголошення')
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,
                               related_name='announcements', verbose_name='Автор')
    created_at = models.DateTimeField('Створено', auto_now_add=True)
    updated_at = models.DateTimeField('Оновлено', auto_now=True)

    class Meta:
        verbose_name = 'Оголошення'
        verbose_name_plural = 'Оголошення'
        ordering = ['-created_at']

    def __str__(self):
        return self.title
