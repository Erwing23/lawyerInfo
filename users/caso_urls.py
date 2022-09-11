from django.urls import path
from . import views

urlpatterns =[
path('stopCaso/<str:id>/', views.stopCaso, name="stopCaso"),
path('tableCaso/updateCaso/<str:id>/', views.updateCaso, name="updateCaso"),
path('updateCaso/<str:id>/', views.updateCaso, name="updateCaso"),
path('deleteCaso/<str:id>/', views.deleteCaso , name="deleteCaso"),
]