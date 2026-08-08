from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import CustomUser

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(
        required=True,
        label='Електронна пошта',
        widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'name@example.com'})
    )
    first_name = forms.CharField(
        required=True,
        label="Ім'я",
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': "Ім'я"})
    )
    last_name = forms.CharField(
        required=True,
        label='Прізвище',
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Прізвище'})
    )
    phone = forms.CharField(
        required=False,
        label='Номер телефону',
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '+380XXXXXXXXX'})
    )
    date_of_birth = forms.DateField(
        required=False,
        label='Дата народження',
        widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date'})
    )
    bio = forms.CharField(
        required=False,
        label='Про себе',
        widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Коротка інформація...'})
    )
    avatar = forms.ImageField(
        required=False,
        label='Аватар',
        widget=forms.FileInput(attrs={'class': 'form-control'})
    )

    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ('username', 'email', 'first_name', 'last_name', 'phone', 'date_of_birth', 'bio', 'avatar')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for name, field in self.fields.items():
            if 'class' not in field.widget.attrs:
                field.widget.attrs['class'] = 'form-control'


class UserLoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': "Ім'я користувача (логин)"
        })
        self.fields['password'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Пароль'
        })


class ProfileUpdateForm(forms.ModelForm):
    date_of_birth = forms.DateField(
        required=False,
        label='Дата народження',
        widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date'})
    )

    class Meta:
        model = CustomUser
        fields = ('first_name', 'last_name', 'email', 'phone', 'date_of_birth', 'bio', 'avatar')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for name, field in self.fields.items():
            if name != 'avatar':
                field.widget.attrs['class'] = 'form-control'
            else:
                field.widget.attrs['class'] = 'form-control'


class UserRoleUpdateForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ('role',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['role'].widget.attrs['class'] = 'form-select'
