from unicodedata import name
from django.shortcuts import render , redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout 
from django.http import HttpResponse


from mainApp.forms import CasoForm
from mainApp.models import PowerUp , User, Caso, Organizacion
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
    username = request.user.username
    #Contexto
    casoQS = Caso.objects.filter(dueñoCaso__username = username)
    form = CasoForm()
    form.fields['organizacionName'].queryset = Organizacion.objects.filter(organizacionUser__username=username)
    context = {"casos":casoQS,"form":form}
    return render(request,"users/tables.html",context)

@login_required
def powerUp(request):
    print(request.user.username+" Request Try")
    return render(request,"users/tables.html")
   

#CRUD DE CASOS
@login_required
def createCaso(request):
    print("Vamos por ese form")
    if request.method == 'POST':
        form = CasoForm(request.POST)
        if form.is_valid():
            caso = form.save(commit=False)
            caso.dueñoCaso = request.user
            form.save()

    return  redirect("/tableCaso")
   
@login_required
def updateCaso(request,id):
    
    print("Caso: ", id)
    context = Caso.objects.get(idCaso = id)
    
    return render(request,"users/update.html")
   

