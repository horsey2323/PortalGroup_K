from django.db import models
from django.conf import settings

class Album(models.Model):
    title = models.CharField(max_length=200, verbose_name="Название альбома")
    description = models.TextField(blank=True, verbose_name="Описание альбома")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, 
        on_delete=models.CASCADE, 
        related_name="albums", 
        verbose_name="Автор"
    )

    class Meta:
        verbose_name = "Альбом"
        verbose_name_plural = "Альбомы"
        ordering = ['-created_at']

    def __str__(self):
        return self.title


class Photo(models.Model):
    album = models.ForeignKey(
        Album, 
        on_delete=models.CASCADE, 
        related_name="photos", 
        verbose_name="Альбом"
    )
    image = models.ImageField(upload_to="gallery/", verbose_name="Изображение")
    caption = models.CharField(max_length=255, blank=True, verbose_name="Подпись к фото")
    uploaded_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата загрузки")
    uploaded_by = models.ForeignKey(
        settings.AUTH_USER_MODEL, 
        on_delete=models.CASCADE, 
        verbose_name="Загрузил"
    )

    class Meta:
        verbose_name = "Фотография"
        verbose_name_plural = "Фотографии"
        ordering = ['-uploaded_at']

    def __str__(self):
        return f"Фото в альбоме '{self.album.title}' ({self.caption or 'Без названия'})"
