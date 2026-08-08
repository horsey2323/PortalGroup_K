from django.urls import path
from . import views

app_name = 'materials'

urlpatterns = [
    path('', views.MaterialListView.as_view(), name='list'),
    path('create/', views.MaterialCreateView.as_view(), name='create'),
    path('<int:pk>/', views.MaterialDetailView.as_view(), name='detail'),
    path('<int:pk>/edit/', views.MaterialUpdateView.as_view(), name='edit'),
    path('<int:pk>/delete/', views.MaterialDeleteView.as_view(), name='delete'),
]
