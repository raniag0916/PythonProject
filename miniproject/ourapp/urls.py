from django.urls import path
from .import views

urlpatterns = [
    path("welcome/",views.welcome,name="welcome"),
    path("oddeven/<int:num>/",views.oddeven,name="oddeven"),
    path("largest/<int:x>/<int:y>/<int:z>",views.largest,name="largest"),
    path("index/",views.index,name="index"),
    path("multiplication/<int:n>",views.multipication, name="multiplication"),

    path("Employee/",views.Employee,name="Employee"),
    path("employeedata/",views.employeedata,name="employeedata"),
    path("DisplayEmployee/",views.DisplayEmployee,name="DisplayEmployee"),
    path("deleteemp/<int:objid>",views.deleteemp,name="deleteemp"),
    path("updateemp/<int:objid>",views.updateemp,name="updateemp"),
    path("updatedata/<int:objid>",views.updatedata,name="updatedata"),
    
    path("StudentDetails/",views.StudentDetails,name="StudentDetails"),
    path("studentdata/",views.studentdata,name="studentdata"),
    path("DisplayStudent/",views.DisplayStudent,name="DisplayStudent"),
    path("deletestud/<int:obid>",views.deletestud,name="deletestud"),
    path("updatestud/<int:obid>",views.updatestud,name="updatestud"),
    path("studentupdate/<int:obid>",views.studentupdate,name="studentupdate")
   
    
    
]