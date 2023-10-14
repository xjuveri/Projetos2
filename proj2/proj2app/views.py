from django.shortcuts import render
from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.db import models

# Create your views here.

def home(request):
  
    return render(request, 'home.html')
  