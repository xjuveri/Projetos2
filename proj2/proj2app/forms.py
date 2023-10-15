from django import forms

class MeuFormulario(forms.Form):
    Email = forms.EmailField(max_length=100)
    Senha = forms.CharField()