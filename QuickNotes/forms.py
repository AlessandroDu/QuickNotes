from django import forms
from django.forms import ModelForm
from .models import Note

class UploadForm(ModelForm):
    class Meta:
        model = Note
        fields = ['name', 'content']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'note-title', 'placeholder': 'New Note'}),
            'content': forms.Textarea(attrs={'class': 'note-content', 'placeholder': 'Write your notes here...'}),
        }