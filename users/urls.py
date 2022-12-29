#users/urls.py

from django.urls import path, include
from . import views, caso_urls
urlpatterns = [

 path('', views.tableCaso, name = "home"),
 path('salir/', views.salir, name="salir"),

 path('tableCaso/', views.tableCaso, name="tableCaso"),
 path('tableCaso/createCaso/', views.createCaso, name="createCaso"),
 path('tableContactos/', views.tableContacto, name="tableContacto"),
 path('tableContactos/createContacto/', views.createContacto, name="tableContacto"),
 path('tableOrganizaciones/', views.tableOrganizacion, name="tableOrganizacion"),
 path('tableOrganizaciones/createOrganizacion/', views.createOrganizacion, name="tableOrganizacion"),

 path('file/<str:id>', views.file, name="file"),
 path('download/<str:id>', views.download, name="download"),


 path('powerUps/', views.powerUp, name="powerUp"),


 path("",include("users.caso_urls")),

]