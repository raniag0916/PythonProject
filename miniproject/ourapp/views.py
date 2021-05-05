from django.shortcuts import render,redirect
from django.http import HttpResponse
from ourapp.models import Student, EmployeeDetails 
from django.core.files.storage import FileSystemStorage
from django.utils.datastructures import MultiValueDictKeyError
# Create your views here.
def welcome(request):
    return HttpResponse("<h5>WELCOME HOME</h5>")

def oddeven(request,num):
    if (num % 2 == 0):
        return HttpResponse("<h3>NUMBER IS EVEN</h3>")
    else:
        return HttpResponse("<h3>NUMBER IS ODD</h3>")

def largest(request,x,y,z):
   
    if (x>y) and (x>z):
        return HttpResponse("<h4> X IS LARGEST </h4>")
    elif (y>x) and (y>z):
        return HttpResponse("<h4> Y IS LARGEST</h4>")
    else:
        return HttpResponse("<h4> Z IS LARGEST</h4")
def index(request):
    name="anju"
    return render(request,'index.html',{'n':name})
def multipication(request,n):
    s = 1
    list1 =[]
    while(s <= 10):
        i = s * n
        list1.append("<br>{} * {} = {}<br>".format(s, n, i))
        s += 1
    return HttpResponse( list1)

def StudentDetails(request):
    return render(request,'StudentDetails.html')

def Employee(request):
    return render(request,'EmployeeDetails.html')

def employeedata(request):
    print("+++++++++++++++++++++++++++++++++++++=")
    if request.method == "POST":
        Name=request.POST.get('ename')
        print("======================",Name)
        Email=request.POST.get('eid')
        Password=request.POST.get('pass')
        Address=request.POST.get('address')
        Gender=request.POST.get('gen')
        PNnumber=request.POST.get('pnumber')
        Image=request.FILES['eimage']
        print(Name,Email)
        ob1=EmployeeDetails(emp_Name=Name,emp_Email=Email,emp_Password=Password,emp_Address=Address,emp_Gender=Gender,emp_PNumber=PNnumber,emp_Image=Image)
        ob1.save()
        return HttpResponse("DONE")
        
def studentdata(request):
    print("uuuuuuuuuuuuuuuuuuuuuuuuuuuuu")
    if request.method == "POST":
        print("rrrrrrrrr")
        a=request.POST.get('sname')
        print("======================",a)
        b=request.POST.get('saddr')
        c=request.POST.get('seid')
        d=request.POST.get('spass')
        e=request.POST.get('sdist')
        f=request.POST.get('sgen')
        print("gender")
        g=request.FILES['image']
        ob2=Student(stud_Name=a,stud_Address=b,stud_Email=c,stud_Password=d,stud_Dist=e,stud_Gender=f,stud_image=g)
        ob2.save()
        return HttpResponse("DONE")
        
def DisplayEmployee(request):
    data=EmployeeDetails.objects.all()
    print("=======================",data)
    for i in data:
        print("**************",i)
        print("$$$$$$$$$$$$$$$$",i.emp_Name)
    return render(request, 'EmployeeDisplay.html',{'data':data})


def deleteemp(request,objid):
    data=EmployeeDetails.objects.filter(id=objid)
    data.delete()
    return redirect(DisplayEmployee)


def updateemp(request,objid):
    data=EmployeeDetails.objects.filter(id=objid)
    return render(request,'updateemployee.html',{'data':data})

    
def updatedata(request,objid):
     if request.method == "POST":
        Name=request.POST.get('ename')
        print("======================",Name)
        Email=request.POST.get('eid')
        Password=request.POST.get('pass')
        Address=request.POST.get('address')
        Gender=request.POST.get('gen')
        PNnumber=request.POST.get('pnumber')
        try:
            Image=request.FILES['eimage']
            # create a new instance of FileSystemStorage 
            fs = FileSystemStorage() 
            file = fs.save(Image.name, Image)
        except MultiValueDictKeyError:
            file =EmployeeDetails.objects.get(id=objid).emp_Image
        print(Name,Email)
        EmployeeDetails.objects.filter(id=objid).update(emp_Name=Name,emp_Email=Email,emp_Password=Password,emp_Address=Address,emp_Gender=Gender,emp_PNumber=PNnumber,emp_Image=file)
        return redirect(DisplayEmployee)

def DisplayStudent(request):
    sdata = Student.objects.all()
    for x in sdata:
        print("***************", x)
        print("@@@@@@@@@@", x.stud_Name)
    return render(request, 'StudentDisplay.html', {'sdata' : sdata})

def deletestud(request, obid):
    sdata = Student.objects.filter(id=obid)
    sdata.delete()
    return redirect(DisplayStudent)

def updatestud(request, obid):
    sdata = Student.objects.filter(id=obid)
    return render(request, 'updatestudent.html', { 'sdata' : sdata})

def studentupdate(request, obid):
    if request.method == "POST":
        a=request.POST.get('sname')
        b=request.POST.get('saddr')
        c=request.POST.get('seid')
        d=request.POST.get('spass')
        e=request.POST.get('sdist')
        f=request.POST.get('sgen')
        # if image need to be updated then try block will execute else if already inserted image need to be 
        # display then except part will get execute
        try:
            g=request.FILES['image']
            # create a new instance of FileSystemStorage 
            fs = FileSystemStorage() 
            file = fs.save(g.name, g)
        except MultiValueDictKeyError:
            file =Student.objects.get(id=obid).stud_image
       
        Student.objects.filter(id=obid).update(stud_Name=a,stud_Address=b,stud_Email=c,stud_Password=d,stud_Dist=e,stud_Gender=f,stud_image=file)
        return redirect(DisplayStudent)







