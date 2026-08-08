from django import forms

from .models import Announcement


class AnnouncementForm(forms.ModelForm):
    class Meta:
        model = Announcement
        fields = ('title', 'content')
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Наприклад: Зміна розкладу пар'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'rows': 7, 'placeholder': 'Напишіть важливу інформацію для групи…'}),
        }
