from unicodedata import name
from django.shortcuts import render , redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout 
from django.http import HttpResponse

from mainApp.models import PowerUp , User
import requests

# Create your views here.
@login_required
def home(request):
    return render(request,"users/index.html")

def salir(request):
    username = request.user.username
    pw = PowerUp.objects.filter(User__username = username)

    print(pw)
    logout(request)
    return redirect("/")

@login_required
def tableCaso(request):
    return render(request,"users/tables.html")

def powerUp(request):
   
    print(request.user.username)
    return "Hello"
   # return render(request,"users/tables.html")

