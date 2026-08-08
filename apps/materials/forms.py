from django import forms

from .models import Material


class MaterialForm(forms.ModelForm):
    class Meta:
        model = Material
        fields = ('title', 'description', 'file')
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Наприклад: Конспект лекції №3'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'placeholder': 'Коротко опишіть матеріал (необов’язково)'}),
            'file': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }

    def clean_file(self):
        file = self.cleaned_data.get('file')
        if file and file.size > 20 * 1024 * 1024:
            raise forms.ValidationError('Розмір файлу не може перевищувати 20 МБ.')
        return file
