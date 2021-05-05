from django.db import models
from dashboard.models import CategoryRegister, ProductRegister, RecipeRegister 

# Create your models here.


class RegisterUser(models.Model):
    Customer_Name = models.CharField(max_length=200, null=True, blank=True)
    Customer_Phone = models.IntegerField(null=True, blank=True)
    Customer_Email = models.EmailField(max_length=200, null=True, blank=True)
    Customer_Username = models.CharField(max_length=200, null=True, blank=True)
    Customer_Password = models.CharField(max_length=200, null=True,blank=True)
    Customer_Cpassword = models.CharField(max_length=200, null=True, blank=True)
    Customer_Address = models.CharField(max_length=200, null=True, blank=True)
    Customer_State = models.CharField(max_length=200, null=True, blank=True)
    Customer_Country = models.CharField(max_length=200, null=True, blank=True)
    Customer_Zip = models.CharField(max_length=200, null=True, blank=True)

class Cart(models.Model):
    Productid = models.ForeignKey(ProductRegister, on_delete=models.CASCADE,null=True,blank=True)
    Userid = models.ForeignKey(RegisterUser, on_delete=models.CASCADE, null=True,blank=True)
    Cart_Quantity = models.IntegerField(null=True, blank=True)
    Cart_Price = models.IntegerField(null=True, blank=True)
    Status = models.IntegerField(null=True,blank=True)

class Order(models.Model):
    Cartid = models.ForeignKey(Cart, on_delete=models.CASCADE, null=True, blank=True)
    Order_Name = models.CharField(max_length=200, null=True, blank=True)
    Order_Uname = models.CharField(max_length=200, null=True, blank=True)
    Order_Email = models.EmailField(max_length=200, null=True, blank=True)
    Order_Address = models.CharField(max_length=200, null=True, blank=True)
    Order_Phone = models.IntegerField(null=True, blank=True)
    Order_State = models.CharField(max_length=200, null=True, blank=True)
    Order_Country = models.CharField(max_length=200, null=True, blank=True)
    Order_Zip = models.CharField(max_length=200, null=True, blank=True)
    Status = models.IntegerField(null=True, blank=True)

class Message(models.Model):
    Message_Name = models.CharField(max_length=200, null=True, blank=True)
    Message_Email = models.EmailField(max_length=200, null=True, blank=True)
    Message_Subject = models.CharField(max_length=200, null=True, blank=True)
    Message_Content = models.CharField(max_length=250, null=True, blank=True)




