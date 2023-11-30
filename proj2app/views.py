from django.shortcuts import render
from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.db import models
from .forms import MeuLogin, MeuCadastro
from .models import ProgressoAluno
from django.contrib.auth.forms import UserCreationForm
from .models import PerfilGestor, PerfilEducador

# Create your views here.

def home(request):
  return render(request, 'home.html')

def login(request):
    if request.method == 'POST':
        form = MeuLogin(request.POST)
        if form.is_valid():
            user_type = form.cleaned_data['user_type']
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            
            # Faça a autenticação com base no tipo de usuário
            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                # Redirecione para a página apropriada com base no tipo de usuário
                if user_type == 'gestor':
                    return HttpResponseRedirect('/perfil_gestor/')
                elif user_type == 'educador':
                    return HttpResponseRedirect('/perfil_educador/')
            else:
                # Tratamento para autenticação falhada
                pass
    else:
        form = MeuLogin()

    return render(request, 'login.html', {'form': form})

def login_gestor(request):
    if request.method == 'POST':
        form = MeuLogin(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            # Lógica de autenticação específica para gestor
            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return HttpResponseRedirect('/dashboard-gestor/')
            else:
                # Tratamento para autenticação falhada
                pass
    else:
        form = MeuLogin()

    return render(request, 'login_gestor.html', {'form': form})
    

def login_educador(request):
    if request.method == 'POST':
        form = MeuLogin(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            # Lógica de autenticação específica para gestor
            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return HttpResponseRedirect('/perfil_educador/')
            else:
                # Tratamento para autenticação falhada
                pass
    else:
        form = MeuLogin()

    return render(request, 'login_educador.html', {'form': form})

def perfil_gestor(request):
    return render(request, 'perfil_gestor.html')

def perfil_educador(request):
    return render(request, 'perfil_educador.html')

#----------------------------------------------
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
def turmas(request):
    return render(request,'turmas.html')
def comoAjudar(request):
    return render(request,'comoAjudar.html')
