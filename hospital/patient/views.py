from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login
from.models import Appointments
from patient.models import Appointments

# Create your views here.




def Phome(request):

    Patient = request.POST.get('Patient')
    
    Date =  request.POST.get('Date')

    Time = request.POST.get('Time') 
   
    Doctor =request.POST.get('Doctor')
    
    data = Appointments(Patient = Patient, Date = Date, Time = Time, Doctor = Doctor)
    data.save()
    return redirect('/patient/patient signin')
 

    

    return render(request,'pages/patinthome.html')


def Plogin(request):

    if request.method== "POST":
        pusername = request.POST.get('pusername')
        ppassword1 = request.POST.get('ppassword1')

        user = authenticate(username=pusername,password=ppassword1)

        if user is not None:
            login(request,user)
            pusername=user.username
            pfname=user.first_name
            plname=user.last_name
            pemail=user.email
            return render(request,'pages/patinthome.html',{'pusername':pusername,'pfname':pfname,'plname':plname,'pemail':pemail})




        else:
            messages.error(request,"error")
            return redirect('/patient/patient signin')


    

    return render(request,'pages/signin.html')


def Psignup(request):

    if request.method == "POST":
        pusername = request.POST['pusername']
        pfname = request.POST['pfname']
        plname = request.POST['plname']
        pemail = request.POST['pemail']
        ppassword1 = request.POST['ppassword1']
        ppassword2 = request.POST['ppassword2']

        patient=User.objects.create_user(pusername,pemail,ppassword1)
        patient.first_name = pfname
        patient.last_name = plname

        patient.save()

        messages.success(request,"Your account has been created successfully")

        return redirect('/patient/patient signin')
    

    return render(request,'pages/signup.html')


