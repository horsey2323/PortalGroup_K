from django.db import models
from django.conf import settings


class ForumCategory(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name='Назва теми')
    description = models.TextField(blank=True, verbose_name='Опис')
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='created_forum_categories',
        verbose_name='Створив',
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата створення')

    class Meta:
        verbose_name = 'Категорія форуму'
        verbose_name_plural = 'Категорії форуму'
        ordering = ['name']

    def __str__(self):
        return self.name


class ForumMessage(models.Model):
    category = models.ForeignKey(
        ForumCategory,
        on_delete=models.CASCADE,
        related_name='messages',
        verbose_name='Категорія',
    )
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='forum_messages',
        verbose_name='Автор',
    )
    text = models.TextField(verbose_name='Повідомлення')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата')

    class Meta:
        verbose_name = 'Повідомлення форуму'
        verbose_name_plural = 'Повідомлення форуму'
        ordering = ['created_at']

    def __str__(self):
        return f'{self.author} - {self.category} ({self.created_at:%d.%m.%Y %H:%M})'
