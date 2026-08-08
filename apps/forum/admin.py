from django.contrib import admin
from .models import ForumCategory, ForumMessage


@admin.register(ForumCategory)
class ForumCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_by', 'created_at')
    search_fields = ('name',)


@admin.register(ForumMessage)
class ForumMessageAdmin(admin.ModelAdmin):
    list_display = ('category', 'author', 'created_at')
    list_filter = ('category',)
    search_fields = ('text',)
