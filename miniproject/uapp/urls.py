from django.urls import path
from .import views
urlpatterns = [
    path("Hai/",views.hai,name="Hai"),
    path("Login/",views.Login,name="Login"),
    # removed / kept ""-field empty inorder to get htmlpage automatically without assigning the name of html page
    path("",views.Registration,name="Registration"),
    path("Registerdata/",views.Registerdata,name="Registerdata"),
    path('login/',views.login,name="login"),
    path('logout/',views.logout,name="logout"),
    path('home/',views.home,name="home")


    
   
]
