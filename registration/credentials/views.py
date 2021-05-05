from django.shortcuts import render, redirect
from credentials.models import RegistrationDetails

# Create your views here.
def Registration(request):
    if request.method == "POST":
        Name = request.POST.get('pname')
        DOB = request.POST.get('birthday')
        Address = request.POST.get('address')
        Email = request.POST.get('eid')
        Password = request.POST.get('pass')
        CPassword = request.POST.get('cpass')
        Gender = request.POST.get('gen')
        if Password == CPassword:
            obj = RegistrationDetails(reg_Name=Name, reg_DOB=DOB, reg_Address=Address, reg_Email=Email,
                                      reg_Password=Password, reg_CPassword=CPassword, reg_Gender=Gender)
            obj.save()
            print('user created')
        else:
            print('Password not match')
    return render(request, 'register.html')


def Login(request):
    return render(request, 'login.html')






