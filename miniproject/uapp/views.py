from django.shortcuts import render, redirect
from django.http import HttpResponse
#import models here.
from uapp.models import RegistrationDetails
# Create your views here.
def hai(request):
    return HttpResponse("<h3>Hai</h3>")
def Login(request):
    return render(request, 'login.html')
#function to render html page
def Registration(request):
    return render(request, 'Registration.html')
#function to insert values to RegistrationDetails model
def Registerdata(request):
    if request.method == "POST":
        Name=request.POST.get('pname')
        DOB=request.POST.get('birthday')
        Address=request.POST.get('address')
        Email=request.POST.get('eid')
        Password=request.POST.get('pass')
        PNnumber=request.POST.get('pnumber')
        Gender=request.POST.get('gen')
        State=request.POST.get('state')
        District=request.POST.get('district')
        obj=RegistrationDetails(reg_Name=Name,reg_DOB=DOB,reg_Address=Address,reg_Email=Email,reg_Password=Password,reg_PNumber=PNnumber,reg_Gender=Gender,reg_State=State,reg_District=District)
        obj.save()
        return redirect(Login)
#login verification here check login details from RegistrationDetails model 
def login(request):
    if request.method == 'POST':
        print("ghhhhhhhhhhhhhhhh")
        email=request.POST.get('email')
        password=request.POST.get('pass')
        if RegistrationDetails.objects.filter(reg_Email=email,reg_Password=password).exists():
            data=RegistrationDetails.objects.filter(reg_Email=email,reg_Password=password).values('reg_Name','reg_DOB','reg_Address')
            print("sssssssssssssssssss",data)
            #check sessions when needed
            request.session['email']=email
            request.session['pass']=password
            request.session['name']=data[0]['reg_Name']
            request.session['dob']=data[0]['reg_DOB']
            print(request.session.get('email'))

            return redirect(home)
        else:
            return render(request,'login.html',{'message':"Invalid username or password"})
def home(request) :
    if 'email' in request.session:
        return render(request,'home.html')
    else:
        return redirect(Login)
def logout(request):
    del request.session['email']
    del request.session['dob']
    del request.session['pass']
    del request.session['name']
    return redirect(Login)