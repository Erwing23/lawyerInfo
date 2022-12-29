from unicodedata import name
from django.shortcuts import render , redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout 
from django.http import HttpResponse, FileResponse
from django.db.models import Q

from mainApp.forms import CasoForm, ContactoForm, OrganizacionForm, FileForm
from mainApp.models import PowerUp , User, Caso, Organizacion, Contacto, Aprobaciones, File
import requests
import datetime


# Create your views here.
@login_required
def home(request):
    return render(request,"users/index.html")

def salir(request):
    print(request.__dict__)
    logout(request)
    return redirect("/")
#Rendering Caso
@login_required
def tableCaso(request):
    username = request.user.username
    #Contexto
    casoQS = Caso.objects.filter(~Q(status='CERR'),dueñoCaso__username = username)
    form = CasoForm()
    form.fields['organizacionName'].queryset = Organizacion.objects.filter(organizacionUser__username=username)

    casos = [
    {'aprobaciones': Aprobaciones.objects.filter(caso__id = caso.pk),
    'id': caso.pk, 
    'organizacionName': caso.organizacionName, 
    'tramite': caso.tramite, 
    'status': caso.get_status_display(),
    'fecha_inicio' : caso.fecha_inicio,
    'fecha_fin' : caso.fecha_fin,
    } 
    for caso in casoQS]
    context = {"casos":casos,"form":form}
    return render(request,"users/tables.html",context)

#Rendering Contactos
@login_required
def tableContacto(request):
    username = request.user.username
    #Contexto
    contactoQS = Contacto.objects.filter(User__username = username)
    form = ContactoForm()
    form.fields['organizacionName'].queryset = Organizacion.objects.filter(organizacionUser__username=username)
    context = {"contactos":contactoQS,"form":form}
    return render(request,"users/tableContactos.html",context)

#Rendering Organizaciones
@login_required
def tableOrganizacion(request):
    username = request.user.username
    #Contexto
    organizacionQS = Organizacion.objects.filter(organizacionUser__username = username)
    form = OrganizacionForm()
    context = {"organizaciones":organizacionQS,"form":form}
    return render(request,"users/tableOrganizaciones.html",context)


@login_required
def powerUp(request):
    print(request.user.username+" Request Try")
    return render(request,"users/powerUps.html")
   

#CRUD DE CASOS
@login_required
def createCaso(request):
    if request.method == 'POST':
        form = CasoForm(request.POST)
        if form.is_valid():
            caso = form.save(commit=False)
            caso.dueñoCaso = request.user
            form.save()

    return  redirect("/tableCaso")

def stopCaso(request, id):
    """
    Cambiar el estado del caso(id) a INACTIVO
    """
    caso = Caso.objects.get(pk = id)
    if caso.dueñoCaso != request.user:
        return redirect("/tableCaso")
    caso.status = "INACTIVO" 
    caso.fecha_fin = datetime.date.today()
    caso.save()
    return  redirect("/tableCaso")

def deleteCaso(request, id):
    """
    Cambiar el estado del caso(id) a CERRADO
    """
    caso = Caso.objects.get(pk = id)
    if caso.dueñoCaso != request.user:
        return redirect("/tableCaso")
    caso.status = "CERR" 
    caso.save()
    return  redirect("/tableCaso")


@login_required
def updateCaso(request,id):
    
    print("Caso: ", id)
    caso = Caso.objects.get(idCaso = id)
   
    return render(request,"users/update.html")
   

#CRUD CONTACTO
@login_required
def createContacto(request):
    if request.method == 'POST':
        form = ContactoForm(request.POST)
        if form.is_valid():
            contacto = form.save(commit=False)
            contacto.User = request.user
            form.save()

    return  redirect("/tableContactos")


#CRUD Organizaciones
@login_required
def createOrganizacion(request):
    if request.method == 'POST':
        form = OrganizacionForm(request.POST)
        if form.is_valid():
            organizacion = form.save(commit=False)
            organizacion.organizacionUser = request.user
            form.save()

    return  redirect("/tableOrganizaciones")

@login_required
def file(request,id):
    username = request.user.username
    caso = Caso.objects.get(pk = id)
    if caso.dueñoCaso != request.user:
        return redirect("/tableCaso")
    if(request.method == 'POST'):
        form = FileForm(request.POST,request.FILES)
        if form.is_valid():
            fileCaso = form.save(commit = False)
            fileCaso.User = request.user
            fileCaso.caso = caso

            form.save()
        return redirect("/file/"+id)
    else:
        #Contexto
        form = FileForm()
    fileQS = File.objects.filter(caso__id = id)
    context = {"form":form,"files":fileQS,"id":id}    
    return render(request,"users/files.html",context)

@login_required
def download(request, id):
    obj = File.objects.get(id=id)
    filename = obj.file.path
    response = FileResponse(open(filename, 'rb'))
    return response