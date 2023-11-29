from django.shortcuts import render
from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.db import models
from .forms import MeuLogin, MeuCadastro
from .models import ProgressoAluno

# Create your views here.

def home(request):
  return render(request, 'home.html')

def login(request):
    if request.method == 'POST':
        form = MeuLogin(request.POST)
        if form.is_valid():
            return redirect('home.html')
    else:
        form = MeuLogin()

    return render(request, 'login.html', {'form': form})
  
def cadastro(request):
    if request.method == 'POST':
        form = MeuCadastro(request.POST)

        if form.is_valid():
            form.save()

            return redirect('login')
    else:
        form = MeuCadastro()

    return render(request, 'cadastro.html', {
        'form': form
    })

def prestacao(request):
    return render(request,'prestacao.html')

def eventos(request):
    return render(request, 'eventos.html')

def grafico(request):
    return render(request, 'grafico.html')
