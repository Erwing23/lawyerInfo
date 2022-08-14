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


 path('tableContactos/', views.tableCaso, name="tableContactos"),


 path('tableOrganizaciones/', views.tableCaso, name="tableContactos"),



 path('tableCaso/powerUp/', views.powerUp, name="powerUp"),



]