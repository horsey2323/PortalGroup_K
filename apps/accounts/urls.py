from django.urls import path
from .views import (
    register_view,
    login_view,
    logout_view,
    profile_view,
    profile_edit_view,
    user_list_view,
    user_role_edit_view
)

app_name = 'accounts'

urlpatterns = [
    path('register/', register_view, name='register'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('profile/', profile_view, name='profile'),
    path('profile/<int:pk>/', profile_view, name='profile_detail'),
    path('profile/edit/', profile_edit_view, name='profile_edit'),
    path('users/', user_list_view, name='user_list'),
    path('users/<int:pk>/role/', user_role_edit_view, name='user_role_edit'),
]
