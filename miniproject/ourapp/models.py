from django.db import models

# Create your models here.
class Student(models.Model):
    stud_Name=models.CharField(max_length=20,null=True,blank=True)
    stud_Address=models.CharField(max_length=20,null=True,blank=True)
    stud_Email=models.EmailField(max_length=20,null=True,blank=True)
    stud_Password=models.CharField(max_length=20,null=True,blank=True)
    stud_Dist=models.CharField(max_length=20,null=True,blank=True)
    stud_Gender=models.CharField(max_length=20,null=True,blank=True)
    stud_image=models.ImageField(upload_to="studentimage",null=True,blank=True)


class Studentmark(models.Model):
    stuentid=models.ForeignKey(Student,on_delete=models.CASCADE)
    studmark=models.IntegerField(null=True,blank=True)

    def __str__(self):
        return self.stuentid.Name

class EmployeeDetails(models.Model):
    emp_Name=models.CharField(max_length=20,null=True,blank=True)
    emp_Email=models.EmailField(max_length=20,null=True,blank=True)
    emp_Password=models.CharField(max_length=20,null=True,blank=True)
    emp_Address=models.CharField(max_length=20,null=True,blank=True)
    emp_Gender=models.CharField(max_length=20,null=True,blank=True)
    emp_PNumber=models.CharField(max_length=20,null=True,blank=True)
    emp_Image=models.ImageField(upload_to="employeeimage",null=True,blank=True)
    
    

class EmployeeSalary(models.Model):
    Salary=models.CharField(max_length=20,null=True,blank=True)
    Empid=models.ForeignKey(EmployeeDetails, on_delete=models.CASCADE)

    def __str__(self):
        return self.Empid.Name




