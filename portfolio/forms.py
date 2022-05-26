from django import forms
from django.forms import ModelForm
from .models import Post, Cadeira


class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = '__all__'
        # inserção de classes CSS para formatação de cada campo do formulário
        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'insert title...'}),
            'descricao': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'insert text...'}),
            'link': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'e.g http...'}),
            'autor': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'e.g John...'}),

        }

        # texto a exibir junto à janela de inserção
        labels = {
            'titulo': 'Title',
            'descricao': 'Description',
            'link': 'Link',
            'autor': 'Autor',
        }

        # texto auxiliar a um determinado campo do formulário
        help_texts = {
            'link': '*optional',
        }


class CadeiraForm(ModelForm):
    class Meta:
        model = Cadeira
        fields = '__all__'
