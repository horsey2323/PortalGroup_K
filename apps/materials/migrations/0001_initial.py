from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True
    dependencies = [migrations.swappable_dependency(settings.AUTH_USER_MODEL)]
    operations = [
        migrations.CreateModel(
            name='Material',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=180, verbose_name='Назва матеріалу')),
                ('description', models.TextField(blank=True, verbose_name='Опис')),
                ('file', models.FileField(upload_to='materials/%Y/%m/', verbose_name='Файл')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Додано')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Оновлено')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='materials', to=settings.AUTH_USER_MODEL, verbose_name='Автор')),
            ],
            options={'verbose_name': 'Матеріал', 'verbose_name_plural': 'Матеріали', 'ordering': ['-created_at']},
        ),
    ]
