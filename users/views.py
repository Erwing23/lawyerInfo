from django.shortcuts import render , redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout 
# Create your views here.
@login_required
def home(request):

    return render(request,"users/index.html")

def salir(request):
    print(request.user.get_full_name())
    logout(request)
    return redirect("/home")
