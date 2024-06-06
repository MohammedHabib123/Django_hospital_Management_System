from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def Dlogin(request):
    return render(request,'pages/DoctorLogin.html')

