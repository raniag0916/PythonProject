from django.contrib import admin
from website.models import  RegisterUser, Cart, Order, Message
# Register your models here.

admin.site.register(RegisterUser)
admin.site.register(Cart)
admin.site.register(Order)
admin.site.register(Message)


