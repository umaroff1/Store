from django.contrib import admin
from .models import Cart,CartProducts,Order
# Register your models here.

admin.site.register(Cart)
admin.site.register(CartProducts)
admin.site.register(Order)