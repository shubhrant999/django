from django.db import models
from django.utils.html import format_html
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
 


class Vendor(models.Model):
    id = models.AutoField(primary_key=True)
    userid = models.ForeignKey('auth.User',on_delete="delete")
    name = models.CharField(max_length=200)
    address =  models.CharField(max_length=500)
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    zipcode = models.CharField(max_length=10)
    contact = models.CharField(max_length=15)
    status = models.IntegerField(default=0)

    class Meta:
        verbose_name_plural = "Vendor"

    def __str__(self):
        return self.name

POST_TYPE = (
    ('0', 'Rent'),
    ('1', 'Sale'),
)

class Post(models.Model):
    id = models.AutoField(primary_key=True)   
    vendor_id = models.ForeignKey(Vendor, on_delete="delete")   
    post_type =  models.CharField(max_length=1,choices=POST_TYPE)
    address =  models.CharField(max_length=500, null=True)
    city = models.CharField(max_length=100, null=True)
    country = models.CharField(max_length=100, null=True)
    zipcode = models.CharField(max_length=10, null=True)
    bedroom = models.IntegerField(null=True)
    bathroom = models.IntegerField(null=True)
    garage = models.IntegerField(default=0)
    price = models.FloatField()  
    desc = models.CharField(max_length=200, null=True) 

    class Meta:
        verbose_name_plural = "Property"
    
    def __str__(self):
        return self.desc

class Banner(models.Model):
    id = models.AutoField(primary_key=True)
    bannerfile = models.FileField(upload_to='./static/img', null=True)
    post = models.ForeignKey(Post, on_delete="delete")

    class Meta:
        verbose_name_plural = "Banners"
        verbose_name = "Banner"

    def __str__(self):
        return format_html(u'<img width="100" hieght="100" src="/media/{}" />', self.bannerfile)


class Blog(models.Model):
    id = models.AutoField(primary_key=True)     
    userid = models.ForeignKey('auth.User',on_delete="delete")
    title = models.CharField(max_length=200)
    blog_type =  models.CharField(max_length=100)
    shortDesc = models.CharField(max_length=100, null=True) 
    publishDate = models.DateTimeField(auto_now=False, auto_now_add=True)
    longDesc = RichTextUploadingField(null=True, blank=True)

    class Meta:
        verbose_name_plural = "Blog"
    
    def __str__(self):
        return self.title


class Image(models.Model):
    id = models.AutoField(primary_key=True)
    blogfile = models.FileField(upload_to='./static/img', null=True)
    blog = models.ForeignKey(Blog, on_delete="delete")

    class Meta:
        verbose_name_plural = "Images"
        verbose_name = "Images"

    def __str__(self):
        return format_html(u'<img width="100" hieght="100" src="/media/{}" />', self.blogfile)


class Contact(models.Model):
    id = models.AutoField(primary_key=True)       
    name =  models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    message =  models.CharField(max_length=500, null=True)
    subject = models.CharField(max_length=100, null=True)
    
    class Meta:
        verbose_name_plural = "Contact"
        verbose_name = "Contact"

    def __str__(self):
        return self.subject

















class Buyer(models.Model):
    id = models.BigAutoField(primary_key=True)    
    username = models.CharField(max_length=50, null=True)
    firstname = models.CharField(max_length=100, null=True)
    lastname = models.CharField(max_length=100, null=True)
    email = models.EmailField(max_length=100)
    address =  models.CharField(max_length=200, null=True)
    city = models.CharField(max_length=50, null=True)
    country = models.CharField(max_length=50, null=True)
    status = models.BooleanField(null=True)
    addedDate = models.DateField(auto_now=False, auto_now_add=True)
    lastModified = models.DateTimeField(auto_now=True, auto_now_add=False)
    
    class Meta:
        verbose_name_plural = "Buyer"
    
    def __str__(self):
        return self.username

    
