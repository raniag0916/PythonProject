from django.urls import path
from . import views

urlpatterns = [

    # removed / kept ""-field empty inorder to get htmlpage automatically without assigning the name of html page
    path("", views.Registration, name="Registration"),
    #path("Registerdata/", views.Registerdata, name="Registerdata"),
    path("Login/", views.Login, name="Login"),
    #path('logout/', views.logout, name="logout"),


]
