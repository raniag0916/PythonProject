from django.shortcuts import render,redirect
from django.http import HttpResponse, JsonResponse
from dashboard.models import CategoryRegister, ProductRegister, RecipeRegister
from website.models import  RegisterUser, Cart, Order, Message
from django.core.files.storage import FileSystemStorage
from django.utils.datastructures import MultiValueDictKeyError
from django.views.decorators.csrf import csrf_exempt
from django.db.models import Sum
from django.core.mail import send_mail
from Fishmart import settings

# Create your views here.
#render function for website.html
def website(request):
    pdata = ProductRegister.objects.all()
    if 'userid' in request.session:
        cartdata = Cart.objects.filter(Userid=request.session.get('userid'))
        item = cartdata.count()
        print("..............", item)
        return render(request, 'Website.html', {'pdata' :pdata, 'cartdata' :cartdata, 'item':item})
    else:
        return render(request, 'Website.html', {'pdata' :pdata})

def home(request):
    cdata = CategoryRegister.objects.all()
    pdata = ProductRegister.objects.all()
    if 'userid' in request.session:
        cartdata = Cart.objects.filter(Userid=request.session.get('userid'),Status=0)
        item = cartdata.count()
        print("..............", item)
        return render(request, 'Home.html', {'cdata':cdata, 'pdata' :pdata, 'cartdata' :cartdata, 'item':item})
    else:
        return render(request, 'Home.html', {'cdata':cdata,'pdata' :pdata})

def aboutus(request):
    return render(request, 'AboutUs.html')

def shop(request):
    cdata = CategoryRegister.objects.all()
    pdata = ProductRegister.objects.all()
    return render(request, 'Shop.html', {'cdata':cdata,'pdata':pdata})

def shopdetails(request, ob2id):
    pdata = ProductRegister.objects.filter(id = ob2id)
    return render(request, 'ShopDetails.html', {'pdata': pdata})

def addtocart(request):
    if request.method == "POST":
        CQuantity = request.POST.get('quant')
        CPrice = request.POST.get('cprice')
        Productid=request.POST.get('productid')
        Userid = request.POST.get('userid')
        ob4 = Cart(Cart_Quantity = CQuantity, Cart_Price = CPrice, Productid=ProductRegister.objects.get(id=Productid), Userid=RegisterUser.objects.get(id=Userid), Status = 0)
        ob4.save()
        return redirect(cart)
   
def cart(request):
    if 'userid' in request.session:
        uid=request.session.get('userid')
        print("666666666666", uid)
        cartdata = Cart.objects.filter(Userid=uid,Status=0)
        print("#######3", cartdata)
        total = Cart.objects.filter(Userid=uid,Status=0).aggregate(Sum('Cart_Price'))
        subtotal = total.get('Cart_Price__sum')
        return render(request, 'Cart.html', {'cartdata': cartdata, 'subtotal': subtotal })
    else:
        return redirect(Login)
@csrf_exempt
def cartupdate(request):
    print("vvvvvvvvvvvvxb")
    if request.method == "POST":
        print("****************")
        print(request.POST)
        quant=request.POST.get('quant')
        cpid=request.POST.get('cpid')
        print(cpid)
        pprice = request.POST.get('pprice')
        cartprice = float(pprice) * float(quant)
        print(cartprice) 
        Cart.objects.filter(id=cpid).update(Cart_Quantity=quant,Cart_Price=cartprice)     
        return HttpResponse()

def remove(request, ob4id):
    deldata = Cart.objects.filter(id = ob4id)
    deldata.delete()
    return redirect(cart)

def checkout(request):
    if 'userid' in request.session:
        uid = request.session.get('userid')
        cdata = Cart.objects.filter(Userid=uid,Status=0)
        total = Cart.objects.filter(Userid=uid,Status=0).aggregate(Sum('Cart_Price'))
        subtotal = total.get('Cart_Price__sum')
        return render(request, 'Checkout.html', {'cdata': cdata, 'subtotal': subtotal})
    else:
        return redirect(Login)    

def orderdata(request):
    Name = request.POST.get('cname')
    Username = request.POST.get('username')
    Email = request.POST.get('email')
    Address = request.POST.get('address')
    Phonenumber = request.POST.get('PNumber')
    State = request.POST.get('state')
    Country = request.POST.get('country')
    Zip = request.POST.get('zip')
    Uid=request.session.get('userid')
    print("***********",Uid)
    cartob=Cart.objects.filter(Userid=Uid, Status=0)
    print("//////////////////", cartob)
    for a in cartob:
        obj=Order(Cartid=Cart.objects.get(id=a.id),Order_Name=Name,Order_Uname=Username,Order_Email=Email,Order_Address=Address, Order_Phone=Phonenumber, Order_State=State, Order_Country=Country, Order_Zip= Zip)
        print("############", obj)
        obj.save()
        Cart.objects.filter(id=a.id).update(Status=1)
    return redirect(home)

def myaccount(request):
    return render(request, 'MyAccount.html')

def wishlist(request, ob2id):
    pdata = ProductRegister.objects.filter(id = ob2id)
    return render(request, 'Wishlist.html', {'pdata': pdata})

def recipe(request):
    rdata = RecipeRegister.objects.all()
    return render(request, 'Recipe.html', {'rdata' :rdata})

def recipedetails(request, ob3id):
    rdata = RecipeRegister.objects.filter(id = ob3id)
    return render(request, 'RecipeDetails.html', {'rdata' :rdata})

def gallery(request):
    data = ProductRegister.objects.all()
    return render(request,"Gallery.html",{'data':data})

def imagecategory(request,cat):
    data=ProductRegister.objects.filter(Product_Category = cat)
    return render(request,"Gallery.html",{'data':data})


def contactus(request):
    return render(request, 'ContactUs.html')

@csrf_exempt
def yourmessage(request):
    data = dict()
    if request.method == 'POST':
        print("$$$$$$$$$$$$$$$$$$$$$$$")
        Name = request.POST.get('mname')
        Email = request.POST.get('memail')
        Subject = request.POST.get('msubject')
        Content = request.POST.get('mcontent')
        ob9 = Message(Message_Name=Name , Message_Email=Email, Message_Subject=Subject, Message_Content=Content)
        ob9.save()
        data['message']="Message sussfully send"
        data['error']=1
        return JsonResponse(data)

def Registration(request):
    return render(request, 'Registration.html')
@csrf_exempt
def userregister(request):
    data = dict()
    if request.method == "POST":
        Name = request.POST.get('CName')
        PNumber = request.POST.get('CNumber')
        Email = request.POST.get('CEmail')
        Username = request.POST.get('uname')
        Password = request.POST.get('password')
        Cpassword = request.POST.get('cpassword')
        Address = request.POST.get('CAddress')
        State = request.POST.get('state')
        Country = request.POST.get('country')
        Zip = request.POST.get('zip')
        if RegisterUser.objects.filter(Customer_Phone=PNumber).exists():
            data['message']="Phone number already exist"
            data['error']=0
            return JsonResponse(data)
        if RegisterUser.objects.filter(Customer_Email=Email).exists():
            data['message'] = "Email id already exist"
            data['error'] = 0
            return JsonResponse(data)
        if RegisterUser.objects.filter(Customer_Username=Username).exists():
            data['message'] = "Username already exist"
            data['error'] = 0
            return JsonResponse(data)
        if RegisterUser.objects.filter(Customer_Password=Password).exists():
            data['message'] = "Password already exist"
            data['error'] = 0
            return JsonResponse(data)
        if RegisterUser.objects.filter(Customer_Cpassword=Cpassword).exists():
            data['message'] = "Confirm Password already exist"
            data['error'] = 0
            return JsonResponse(data)        
        obj1 = RegisterUser(Customer_Name=Name, Customer_Phone=PNumber, Customer_Email=Email, Customer_Username=Username, Customer_Password=Password, Customer_Cpassword=Cpassword, Customer_Address=Address,Customer_State=State ,Customer_Country=Country ,Customer_Zip=Zip)
        subject="Registeration"
        message="Thanku for registration"
        from_email=settings.DEFAULT_FROM_EMAIL
        send_mail(subject,message,from_email,[Email],fail_silently=False)
        obj1.save()
        data['message']="sussfully registered"
        data['error']=1
        return JsonResponse(data)


def Login(request):
    return render(request, 'Login.html')

def login(request):
    if request.method == 'POST':
        Username = request.POST.get("uname")
        Password = request.POST.get("password")
        if RegisterUser.objects.filter(Customer_Username=Username, Customer_Password=Password).exists():
            logindata = RegisterUser.objects.filter(Customer_Username=Username, Customer_Password=Password).values('Customer_Name','Customer_Password', 'id').first()
            request.session['uname'] = Username
            request.session['password'] = Password
            request.session['userid'] = logindata['id']
            return redirect(home)
        else:
            return render(request, 'Login.html', {'message': 'Invalid Username or Password'})

def logout(request):
    del request.session['uname']
    del request.session['password'] 
    del request.session['userid'] 
    return redirect(home)






