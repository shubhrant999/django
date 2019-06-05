from django.contrib import admin
from .models import Vendor, Post, Banner, Buyer, Contact, Blog, Image
# from .forms import BannerAdminForm

# class BannerAdmin(admin.ModelAdmin):
#     form = BannerAdminForm

class MyModelAdmin(admin.ModelAdmin):
    readonly_fields=('name','email','message', 'subject')

# Register your models here.
admin.site.register(Vendor)
admin.site.register(Post)
admin.site.register(Banner)
admin.site.register(Buyer)
admin.site.register(Contact, MyModelAdmin)
admin.site.register(Blog)
admin.site.register(Image)