from django.shortcuts import render
from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.db import models

# Create your views here.

def home(request):
    if request.method == "POST":
        return render(request, 'usuarios/home.html')
    elif request.method == "GET":
        return render(request, 'usuarios/home.html')
    else:
        return HttpResponse('erro!')