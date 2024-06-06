from django.contrib import admin
from django.urls import path
from .import views
urlpatterns = [
     

    path('patient signin',views.Plogin, name='Plogin'),
    path('patient signup',views.Psignup, name='Psignup'),
    path('patient home',views.Phome, name='Phome'),
]
