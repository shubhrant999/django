from django.db import models

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

