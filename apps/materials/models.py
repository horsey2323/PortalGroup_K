from django.db import models
from django.conf import settings


class Material(models.Model):
    title = models.CharField('Назва матеріалу', max_length=180)
    description = models.TextField('Опис', blank=True)
    file = models.FileField('Файл', upload_to='materials/%Y/%m/')
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,
                               related_name='materials', verbose_name='Автор')
    created_at = models.DateTimeField('Додано', auto_now_add=True)
    updated_at = models.DateTimeField('Оновлено', auto_now=True)

    class Meta:
        verbose_name = 'Матеріал'
        verbose_name_plural = 'Матеріали'
        ordering = ['-created_at']

    @property
    def extension(self):
        return self.file.name.rsplit('.', 1)[-1].lower() if '.' in self.file.name else ''

    def __str__(self):
        return self.title
