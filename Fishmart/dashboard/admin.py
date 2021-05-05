from django.contrib import admin
from dashboard.models import CategoryRegister, ProductRegister, RecipeRegister
# Register your models here.

admin.site.register(CategoryRegister)
admin.site.register(ProductRegister)
admin.site.register(RecipeRegister)
