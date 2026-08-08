from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import Album

User = get_user_model()

class GalleryModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='password123')
        self.album = Album.objects.create(title='Тестовый альбом', author=self.user)

    def test_album_creation(self):
        self.assertEqual(self.album.title, 'Тестовый альбом')
        self.assertEqual(str(self.album), 'Тестовый альбом')
