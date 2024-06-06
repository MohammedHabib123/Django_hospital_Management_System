from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def alogin(request):
    return render(request,'pages/admission.html')