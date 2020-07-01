from django.db import models
from django.utils import timezone
# Create your models here.

class mark(models.Model):
    user=models.CharField(max_length=30)
    password=models.TextField(max_length=30)
class kitchen(models.Model):
    img=models.ImageField()
    name=models.CharField(max_length=30)
    desc=models.CharField(max_length=70)
    price=models.IntegerField()
class detail(models.Model):
    fname=models.TextField(max_length=10)
    lname=models.TextField(max_length=10)
    uname=models.TextField(max_length=20)
    password=models.TextField(max_length=10)
    email=models.TextField(max_length=20)
    phone=models.IntegerField()
    address=models.TextField(max_length=200)
class product(models.Model):
    img=models.ImageField(upload_to="pic")
    order_id=models.TextField(max_length=10)
class total_product(models.Model):
    product_uid=models.TextField(max_length=34)
    product_name=models.TextField(max_length=15,default="")
    product_cat=models.TextField(max_length=50,default="")
    product_subcat=models.CharField(max_length=50,default="")
    product_img=models.ImageField(upload_to="media")
    puroduct_pubdate=models.DateTimeField()
    product_desc=models.TextField(max_length=150,default="")
    product_price=models.IntegerField(default=0)

    def __str__(self):
        return self.product_name




