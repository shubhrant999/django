from django.contrib import admin
from .models import Category,Vendor,Product

# Register your models here.
admin.site.register(Category)
admin.site.register(Vendor)
admin.site.register(Product)
