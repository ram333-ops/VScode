from django import forms
from .models import Comentario


class ComentarioForm(forms.ModelForm):
    class Meta:
        model = Comentario
        fields = ['nombre', 'email', 'contenido']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Tu nombre'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Tu email institucional'}),
            'contenido': forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'placeholder': 'Tu comentario'}),
        }