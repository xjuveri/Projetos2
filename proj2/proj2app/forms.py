from django import forms

class MeuLogin(forms.Form):
    Email = forms.EmailField(max_length=100)
    Senha = forms.CharField()

class MeuCadastro(forms.Form):
    Email = forms.EmailField(max_length=100)
    Senha = forms.CharField()
    Confirme = forms.CharField()
