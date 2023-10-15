from django.shortcuts import render
from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.db import models
from .forms import MeuFormulario

# Create your views here.

def home(request):
  return render(request, 'home.html')
  

def login(request):
    if request.method == 'POST':
        form = MeuFormulario(request.POST)
        if form.is_valid():
            return redirect('home.html')
    else:
        form = MeuFormulario()

    return render(request, 'login.html', {'form': form})

def cadastro(request):
    if request.method == 'POST':
        form = MeuFormulario(request.POST)
        
        if form.is_valid():
            form.save()
    
            return redirect('login')
    else:
        form = MeuFormulario()
        
    return render(request, 'cadastro.html', {
        'form': form
    })
