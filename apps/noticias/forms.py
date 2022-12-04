from django import forms
from .models import Post


class PosteoForm(forms.ModelForm):
    
    class Meta:
        model = Post
        fields = ['titulo', 'contenido', 'imagen']

        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control'}),
            'imagen': forms.FileInput(attrs={'class': 'form-control'}),
            'contenido': forms.Textarea(attrs={'class':'form-control','cols': 80, 'rows': 5}),
            # 'categoria': forms.RadioSelect(attrs={'class':'form-control'}),
            # 'autor': forms.TextInput(attrs={'class': 'form-control','type': 'hidden', 'id': 'autor', 'value': ''}),
            #'autor': forms.Select(attrs={'class': 'form-control'}),
        }

class EdicionForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['titulo', 'contenido', 'imagen']
        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control'}),
            'contenido': forms.Textarea(attrs={'class':'form-control','cols': 80, 'rows': 5}),
            #'autor': forms.Select(attrs={'class': 'form-control'}),
            # 'categoria': forms.Select(attrs={'class':'form-control'}),
        }
        