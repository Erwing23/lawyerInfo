from django.shortcuts import render , redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout 
from mainApp.models import PowerUp
import requests
# Create your views here.
@login_required
def home(request):

    return render(request,"users/index.html")

def salir(request):
    print(request.user.username)
    logout(request)
    return redirect("/")

@login_required
def tableCaso(request):
    return render(request,"users/tables.html")


@login_required
def powerUp(request):
    print("pilas")
    print(request.user.username)
   # return render(request,"users/tables.html")

