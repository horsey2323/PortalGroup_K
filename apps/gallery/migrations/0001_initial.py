from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True
    dependencies = [migrations.swappable_dependency(settings.AUTH_USER_MODEL)]
    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Назва альбому')),
                ('description', models.TextField(blank=True, verbose_name='Опис альбому')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата створення')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='albums', to=settings.AUTH_USER_MODEL, verbose_name='Автор')),
            ],
            options={'verbose_name': 'Альбом', 'verbose_name_plural': 'Альбоми', 'ordering': ['-created_at']},
        ),
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='gallery/', verbose_name='Зображення')),
                ('caption', models.CharField(blank=True, max_length=255, verbose_name='Підпис до фото')),
                ('uploaded_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата завантаження')),
                ('album', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='photos', to='gallery.album', verbose_name='Альбом')),
                ('uploaded_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Завантажив')),
            ],
            options={'verbose_name': 'Фотографія', 'verbose_name_plural': 'Фотографії', 'ordering': ['-uploaded_at']},
        ),
    ]
