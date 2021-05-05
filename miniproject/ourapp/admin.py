from django.contrib import admin
from ourapp.models import Studentmark,Student,EmployeeDetails,EmployeeSalary

# Register your models here.
admin.site.register(Student)
admin.site.register(Studentmark)
admin.site.register(EmployeeDetails)
admin.site.register(EmployeeSalary)
