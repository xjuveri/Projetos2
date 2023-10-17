from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms  import UserCreationForm

class MeuLogin(forms.Form):
    Email = forms.EmailField(max_length=100)
    Senha = forms.CharField()

class MeuCadastro(UserCreationForm):
    class Meta:
        model = User
        fields = ('username','email', 'password1', 'password2')
        
    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Username'
    }))
    email = forms.CharField(widget=forms.EmailInput(attrs={
        'placeholder': 'E-mail'
    }))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Password'
    }))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Repeat password'
    }))
