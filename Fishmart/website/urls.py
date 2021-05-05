from django.urls import path
from django.contrib import admin
from .import views
urlpatterns = [
    path("website/", views.website, name="website"),
    path("home/", views.home,name="home"),
    path("aboutus/", views.aboutus, name="aboutus"),
    path("shop/", views.shop, name="shop"),
    path("shopdetails/<int:ob2id>", views.shopdetails,name="shopdetails"),
    path("addtocart/", views.addtocart, name="addtocart"),
    path("cart/", views.cart, name="cart"),
    path("cartupdate/", views.cartupdate, name="cartupdate"),
    path("remove/<int:ob4id>", views.remove, name="remove"),
    path("checkout/", views.checkout, name="checkout"),
    path("orderdata/", views.orderdata, name="orderdata"),
    path("myaccount/", views.myaccount, name="myaccount"),
    path("wishlist/<int:ob2id>", views.wishlist, name="wishlist"),
    path("recipe/", views.recipe, name="recipe"),
    path("recipedetails/<int:ob3id>", views.recipedetails, name="recipedetails"),
    path("gallery/", views.gallery,name="gallery"),
    path("imagecategory/<str:cat>", views.imagecategory, name="imagecategory"),
    path("contactus/", views.contactus, name="contactus"),
    path("yourmessage/", views.yourmessage, name="yourmessage"),
    path("Registration/", views.Registration, name="Registration"),
    path("userregister/", views.userregister, name="userregister"),
    path("Login/", views.Login, name="Login"),
    path("login/", views.login, name="login"),
    path("logout/", views.logout, name="logout"),


]
    