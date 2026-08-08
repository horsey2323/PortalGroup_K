from django import forms
from .models import ForumCategory, ForumMessage


class ForumCategoryForm(forms.ModelForm):
    class Meta:
        model = ForumCategory
        fields = ['name', 'description']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Назва теми',
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 3,
                'placeholder': 'Короткий опис теми (необов\'язково)',
            }),
        }

    def clean_name(self):
        name = self.cleaned_data['name'].strip()
        if len(name) < 3:
            raise forms.ValidationError('Назва теми має містити щонайменше 3 символи.')
        return name


class ForumMessageForm(forms.ModelForm):
    class Meta:
        model = ForumMessage
        fields = ['text']
        widgets = {
            'text': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 3,
                'placeholder': 'Напишіть повідомлення...',
            }),
        }
        labels = {
            'text': '',
        }

    def clean_text(self):
        text = self.cleaned_data['text'].strip()
        if len(text) < 2:
            raise forms.ValidationError('Повідомлення не може бути порожнім.')
        if len(text) > 3000:
            raise forms.ValidationError('Повідомлення занадто довге (максимум 3000 символів).')
        return text
