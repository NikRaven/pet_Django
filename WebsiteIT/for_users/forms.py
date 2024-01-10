from .models import UserTable
from django.forms import ModelForm, widgets, TextInput, Textarea, DateTimeInput, PasswordInput
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms


class UsersFrom(ModelForm):
    class Meta:
        model = UserTable
        fields = ['name', 'second_name', 'email', 'password']

        widgets = {
            "name": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ваше имя'
            }),
            "second_name": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ваша фамилия'
            }),
            "email": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Почта'
            }),
            "password": PasswordInput(attrs={
                'class': 'form-control',
                'placeholder': "Пароль"
            })
        }


class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

        widgets = {
            "username": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Имя Пользователя'
            }),
            "email": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Почта'
            }),
            "password1": PasswordInput(attrs={
                'class': 'form-control',
                'placeholder': "Пароль"
            }),
            "password2": PasswordInput(attrs={
                'class': 'form-control',
                'placeholder': "Подтвердите пароль"
            })
        }
