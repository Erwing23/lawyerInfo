#users/urls.py

from django.urls import path
from . import views
urlpatterns = [

 path('', views.home, name = "home"),
 path('salir/', views.salir, name="salir"),

 path('tableCaso/', views.tableCaso, name="tableCaso"),
 path('tableCaso/createCaso/', views.createCaso, name="createCaso"),
 path('tableCaso/updateCaso/<str:id>/', views.updateCaso, name="updateCaso"),
 path('updateCaso/<str:id>/', views.updateCaso, name="updateCaso"),


 path('tableContactos/', views.tableContacto, name="tableContacto"),
 path('tableContactos/createContacto/', views.createContacto, name="tableContacto"),


 path('tableOrganizaciones/', views.tableOrganizacion, name="tableOrganizacion"),
 path('tableOrganizaciones/createOrganizacion/', views.createOrganizacion, name="tableOrganizacion"),



 path('powerUps/', views.powerUp, name="powerUp"),



]