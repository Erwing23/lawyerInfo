#users/urls.py

from django.urls import path
from . import views
urlpatterns = [

 path('', views.home, name = "home"),
 path('salir/', views.salir, name="salir"),
 path('tableCaso/', views.tableCaso, name="tableCaso"),
 path('powerUp/', views.powerUp, name="powerUp"),


]