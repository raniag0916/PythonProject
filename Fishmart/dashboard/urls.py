from django.urls import path
from django.contrib import admin
from .import views
urlpatterns = [
    path("dashboard/", views.dashboard,name="dashboard"),

    path("category_reg/", views.category_reg, name="category_reg"),
    path("categorydata", views.categorydata, name="categorydata"),
    path("DisplayCategory/",views.DisplayCategory,name="DisplayCategory"),
    path("deletecategory/<int:ob1id>",views.deletecategory,name="deletecategory"),
    path("updatecategory/<int:ob1id>",views.updatecategory,name="updatecategory"),
    path("updatecategorydata/<int:ob1id>",views.updatecategorydata,name="updatecategorydata"),

    path("product_reg/", views.product_reg, name="product_reg"),
    path("productdata", views.productdata, name="productdata"),
    path("DisplayProduct/",views.DisplayProduct,name="DisplayProduct"),
    path("deleteproduct/<int:ob2id>",views.deleteproduct,name="deleteproduct"),
    path("updateproduct/<int:ob2id>",views.updateproduct,name="updateproduct"),
    path("updateproductdata/<int:ob2id>",views.updateproductdata,name="updateproductdata"),

    path("recipe_reg/", views.recipe_reg, name="recipe_reg"),
    path("recipedata", views.recipedata, name="recipedata"),
    path("DisplayRecipe/", views.DisplayRecipe, name="DisplayRecipe"),
    path("deleterecipe/<int:ob3id>", views.deleterecipe, name="deleterecipe"),
    path("updaterecipe/<int:ob3id>", views.updaterecipe, name="updaterecipe"),
    path("updaterecipedata/<int:ob3id>", views.updaterecipedata, name="updaterecipedata"),

    path("messagedisplay/", views.messagedisplay, name="messagedisplay"),
    path("oderdisplay/", views.oderdisplay, name="oderdisplay"),
]