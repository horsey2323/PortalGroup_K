from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ('username', 'email', 'first_name', 'last_name', 'role', 'is_staff', 'is_superuser')
    list_filter = ('role', 'is_staff', 'is_superuser', 'is_active')
    search_fields = ('username', 'first_name', 'last_name', 'email')
    ordering = ('username',)

    fieldsets = UserAdmin.fieldsets + (
        ('Додаткова інформація про користувача', {
            'fields': ('role', 'avatar', 'bio', 'phone', 'date_of_birth')
        }),
    )

    add_fieldsets = UserAdmin.add_fieldsets + (
        ('Додаткова інформація', {
            'fields': ('first_name', 'last_name', 'email', 'role', 'avatar', 'bio', 'phone', 'date_of_birth')
        }),
    )
