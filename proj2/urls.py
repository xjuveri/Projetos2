"""
URL configuration for proj2 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.urls import path, include
from proj2app import views

app_name="proj2"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('login/', views.login, name='login'),
    path('cadastro/', views.cadastro, name='cadastro'),
    path('prestacao/',views.prestacao, name= 'prestacao'),
    path('grafico/', views.grafico, name = 'grafico'),
    path('inventario/', include('inventario_patrimonial.urls')),
    path('turmas/', views.turmas, name = 'turmas'),
    path('comoAjudar/', views.comoAjudar, name = 'comoAjudar'),
    path('quemSomos/', views.somos, name = 'quemSomos'),
    path('relatorio/', include('relatorio.urls')),
    #tipos de login
    path('login_gestor', views.login_gestor, name='login_gestor'),
    path('login_educador/', views.login_educador, name='login_educador'),
    path('perfil_gestor/', views.perfil_gestor, name='perfil_gestor'),
    path('perfil_educador/', views.perfil_educador, name='perfil_educador'),

]

