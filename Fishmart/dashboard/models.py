from django.db import models

# Create your models here.
class CategoryRegister(models.Model):
    Category_Name = models.CharField(max_length=200, null=True, blank=True)
    Category_Image = models.ImageField(upload_to="categoryimage", null=True, blank=True)

class ProductRegister(models.Model):
    Product_Name = models.CharField(max_length=200, null=True, blank=True)
    Product_Category = models.CharField(max_length=150, null=True, blank=True)
    Product_Image = models.ImageField(upload_to = "productimage", null=True, blank=True)
    Product_Stock = models.CharField(max_length=50, null=True, blank=True)
    Product_Quantity = models.CharField(max_length=200, null=True, blank=True)
    Product_Price = models.CharField(max_length=150, null=True, blank=True)
    Product_Description = models.CharField(max_length=200, null=True,blank=True)

class RecipeRegister(models.Model):
    Recipe_Name = models.CharField(max_length=200, null=True, blank=True)
    Recipe_Image = models.ImageField(upload_to = "recipeimage", null=True, blank=True)
    Recipe_Ingredient = models.CharField(max_length=200, null=True, blank=True)
    Recipe_Description = models.CharField(max_length=200, null=True, blank=True)
    Recipe_Time = models.CharField(max_length=200, null=True, blank=True)
    Recipe_Calorie = models.CharField(max_length=200, null=True, blank=True)
