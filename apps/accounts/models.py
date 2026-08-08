from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    ROLE_CHOICES = (
        ('user', 'Користувач'),
        ('moderator', 'Модератор'),
        ('admin', 'Адміністратор'),
    )

    role = models.CharField(
        max_length=20,
        choices=ROLE_CHOICES,
        default='user',
        verbose_name='Роль'
    )
    bio = models.TextField(
        blank=True,
        verbose_name='Про себе'
    )
    avatar = models.ImageField(
        upload_to='avatars/',
        blank=True,
        null=True,
        verbose_name='Аватар'
    )
    phone = models.CharField(
        max_length=20,
        blank=True,
        verbose_name='Номер телефону'
    )
    date_of_birth = models.DateField(
        blank=True,
        null=True,
        verbose_name='Дата народження'
    )

    class Meta:
        verbose_name = 'Користувач'
        verbose_name_plural = 'Користувачі'

    def __str__(self):
        return self.username
