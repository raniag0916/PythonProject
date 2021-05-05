from django.db import models


# Create your models here.

class RegistrationDetails(models.Model):
    reg_Name = models.CharField(max_length=20)
    reg_DOB = models.CharField(max_length=20)
    reg_Address = models.CharField(max_length=20)
    reg_Email = models.EmailField(max_length=20)
    reg_Password = models.CharField(max_length=20)
    reg_CPassword = models.CharField(max_length=20)
    reg_Gender = models.CharField(max_length=20)
    
    def __str__(self):
        return self.reg_Name

