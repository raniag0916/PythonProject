from django.db import models

# Create your models here.
class RegistrationDetails(models.Model):
    reg_Name = models.CharField(max_length=20,null=True,blank=True)
    reg_DOB = models.CharField(max_length=20,null=True,blank=True)
    reg_Address = models.CharField(max_length=20,null=True,blank=True)
    reg_Email = models.EmailField(max_length=20,null=True,blank=True)
    reg_Password = models.CharField(max_length=20,null=True,blank=True)
    reg_PNumber = models.CharField(max_length=20,null=True,blank=True)
    reg_Gender = models.CharField(max_length=20,null=True,blank=True)
    reg_State = models.CharField(max_length=20,null=True,blank=True)
    reg_District = models.CharField(max_length=20,null=True,blank=True)