from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from dashboard.models import CategoryRegister, ProductRegister, RecipeRegister 
from website.models import Order, Message, RegisterUser, Cart
from django.core.files.storage import FileSystemStorage
from django.utils.datastructures import MultiValueDictKeyError
from django.views.decorators.csrf import csrf_exempt
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# Create your views here.
def dashboard(request):
    return render(request, 'Dashboard.html')

def category_reg(request):
    return render(request, 'Category_reg.html')

@csrf_exempt
def categorydata(request):
    data = dict()
    if request.method == "POST":
        print("!!!!!!!!!!!!!!!!!")
        Name = request.POST.get('cname')
        Image = request.FILES['cimage']
        if CategoryRegister.objects.filter(Category_Name=Name).exists():
            data['error'] = 0
            data['message'] = "This category already exist!"
            return JsonResponse(data)
        ob1 = CategoryRegister(Category_Name = Name, Category_Image = Image)
        ob1.save()
        data['error'] = 1
        data['message'] = "Sucessfully Registered!!"
        return JsonResponse(data)
    
def DisplayCategory(request):
    datas = CategoryRegister.objects.all()
    page = request.GET.get('page', 1)

    paginator = Paginator(datas, 3)
    try:
        data = paginator.page(page)
    except PageNotAnInteger:
        data = paginator.page(1)
    except EmptyPage:
        data = paginator.page(paginator.num_pages)
    return render(request, 'CategoryDisplay.html',{'data':data})

def deletecategory(request,ob1id):
    data = CategoryRegister.objects.filter(id=ob1id)
    data.delete()
    return redirect(DisplayCategory)

def updatecategory(request,ob1id):
    data=CategoryRegister.objects.filter(id=ob1id)
    return render(request,'UpdateCategory.html',{'data':data})


def updatecategorydata(request,ob1id):
     if request.method == "POST":
        Name=request.POST.get('cname')
        try:
            Image=request.FILES['cimage']
            # create a new instance of FileSystemStorage 
            fs = FileSystemStorage() 
            file = fs.save(Image.name, Image)
        except MultiValueDictKeyError:
            file =CategoryRegister.objects.get(id=ob1id).Category_Image
        print(Name)
        CategoryRegister.objects.filter(id=ob1id).update(Category_Name=Name,Category_Image=file)
        return redirect(DisplayCategory)

def product_reg(request):
    data = CategoryRegister.objects.values('Category_Name')
    print("****************", data)
    return render(request, 'ProductRegister.html', {'data':data})
@csrf_exempt
def productdata(request):
    data=dict()
    print("______________________________")
    if request.method == "POST":
        PName = request.POST.get('pname')
        PCategory = request.POST.get('pcategory')
        PImage = request.FILES['pimage']
        PStock = request.POST.get('pstock')
        PQuantity = request.POST.get('pquantity')
        PPrice = request.POST.get('pprice')
        PDescription = request.POST.get('pdescription')
        if ProductRegister.objects.filter(Product_Name=PName).exists():
            data['error']=0
            data['message']="This product already exist"
            return JsonResponse(data)
        ob2 = ProductRegister(Product_Name=PName, Product_Category=PCategory, Product_Image=PImage, Product_Stock=PStock, Product_Quantity=PQuantity, Product_Price=PPrice, Product_Description=PDescription)
        ob2.save()
        data['error']=1
        data['message']="successfully registered"
        return JsonResponse(data)
def DisplayProduct(request):
    datas= ProductRegister.objects.all()
    page = request.GET.get('page', 1)

    paginator = Paginator(datas, 3)
    try:
        data = paginator.page(page)
    except PageNotAnInteger:
        data = paginator.page(1)
    except EmptyPage:
        data = paginator.page(paginator.num_pages)
    return render(request, 'ProductDisplay.html',{'data':data})

def deleteproduct(request,ob2id):
    data = ProductRegister.objects.filter(id=ob2id)
    data.delete()
    return redirect(DisplayProduct)

def updateproduct(request,ob2id):
    data= ProductRegister.objects.filter(id=ob2id)
    pcat=data.first().Product_Category
    catdata = CategoryRegister.objects.exclude(Category_Name=pcat)
    print("&&&&&&&&&&&&&&",catdata)
    return render(request,'ProductUpdate.html',{'data':data,'catdata':catdata})

def updateproductdata(request,ob2id):
     if request.method == "POST":
        Name=request.POST.get('pname')
        Category=request.POST.get('pcategory')
        try:
            Image=request.FILES['pimage']
            # create a new instance of FileSystemStorage 
            fs = FileSystemStorage() 
            file = fs.save(Image.name, Image)
        except MultiValueDictKeyError:
            file =ProductRegister.objects.get(id=ob2id).Product_Image
        Stock=request.POST.get('pstock')
        Quantity=request.POST.get('pquantity')
        Price=request.POST.get('pprice')
        Description=request.POST.get('pdescription')
        print(Name)
        ProductRegister.objects.filter(id=ob2id).update(Product_Name=Name,Product_Category=Category, Product_Image=file, Product_Stock=Stock,Product_Quantity=Quantity,Product_Price=Price,Product_Description=Description)
        return redirect(DisplayProduct)

def recipe_reg(request):
    return render(request, 'RecipeRegister.html' )
@csrf_exempt
def recipedata(request):
    data = dict()
    if request.method == "POST":
        RName = request.POST.get('rname')
        RImage = request.FILES['rimage']
        RIngredient = request.POST.get('ringredient')
        RDescription = request.POST.get('rdescription')
        RTime = request.POST.get('rtime')
        Rcalorie = request.POST.get('rcalories')
        #here will check if name already exist in database and if exist display a warnning message
        if RecipeRegister.objects.filter(Recipe_Name=RName).exists():
            data['error'] = 0
            data['message'] = "This recipe already exist!"
            return JsonResponse(data)
        ob3 = RecipeRegister(Recipe_Name=RName, Recipe_Image=RImage, Recipe_Ingredient=RIngredient, Recipe_Description=RDescription, Recipe_Time=RTime, Recipe_Calorie=Rcalorie)
        ob3.save()
        data['error'] = 1 
        data['message'] = "Sucessfully Registered!!"
        return JsonResponse(data)

def DisplayRecipe(request):
    datas = RecipeRegister.objects.all()
    page = request.GET.get('page', 1)

    paginator = Paginator(datas, 3)
    try:
        data = paginator.page(page)
    except PageNotAnInteger:
        data = paginator.page(1)
    except EmptyPage:
        data = paginator.page(paginator.num_pages)
    return render(request, 'RecipeDisplay.html',{'data':data})

def deleterecipe(request,ob3id):
    data = RecipeRegister.objects.filter(id=ob3id)
    data.delete()
    return redirect(DisplayRecipe)

def updaterecipe(request,ob3id):
    data= RecipeRegister.objects.filter(id=ob3id)
    return render(request,'RecipeUpdate.html',{'data':data})

def updaterecipedata(request,ob3id):
     if request.method == "POST":
        Name=request.POST.get('rname')
        try:
            Image=request.FILES['rimage']
            # create a new instance of FileSystemStorage 
            fs = FileSystemStorage() 
            file = fs.save(Image.name, Image)
        except MultiValueDictKeyError:
            file =RecipeRegister.objects.get(id=ob3id). Recipe_Image
        Ingredient=request.POST.get('ringredient')
        Description=request.POST.get('rdescription')
        Time=request.POST.get('rtime')
        Calories=request.POST.get('rcalories')
        print(Name)
        RecipeRegister.objects.filter(id=ob3id).update(Recipe_Name=Name, Recipe_Image=file, Recipe_Ingredient=Ingredient,Recipe_Description=Description,Recipe_Time=Time,Recipe_Calorie= Calories)
        return redirect(DisplayRecipe)

def messagedisplay(request):
    datas = Message.objects.all()
    page = request.GET.get('page', 1)

    paginator = Paginator(datas, 3)
    try:
        data = paginator.page(page)
    except PageNotAnInteger:
        data = paginator.page(1)
    except EmptyPage:
        data = paginator.page(paginator.num_pages)
    return render(request, 'MessageDisplay.html', {'data': data})

def oderdisplay(request):
    datas = Order.objects.all()
    page = request.GET.get('page', 1)

    paginator = Paginator(datas, 3)
    try:
        data = paginator.page(page)
    except PageNotAnInteger:
        data = paginator.page(1)
    except EmptyPage:
        data = paginator.page(paginator.num_pages)
    return render(request,'OrderDisplay.html',{'data':data})
     


