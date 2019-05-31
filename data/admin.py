from django.contrib import admin
from .models import Vendor,Post, Banner

# Register your models here.
admin.site.register(Vendor)
admin.site.register(Post)
admin.site.register(Banner)