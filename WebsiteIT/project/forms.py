from .models import Project
from django.forms import ModelForm, widgets, TextInput, Textarea, DateTimeInput, FileField, ImageField, \
    ClearableFileInput


class ProjectFrom(ModelForm):
    class Meta:
        model = Project
        fields = ['title', 'description', 'technology', 'image']  #

        widgets = {
            "title": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Заголовок'
            }),
            "description": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Описание'
            }),
            "technology": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'технология'
            }),
            # "image": ClearableFileInput(),
        }
