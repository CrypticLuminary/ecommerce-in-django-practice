from django.db import models
from django.db.models import Model

# Create your models here.

class category(models.Model):
    category_name = models.CharField(max_length=30, null=True,blank=True)
    category_description = models.TextField()
    # image = models.ImageField(upload_to='category/', null=True, blank=True)
    # image_url = models.URLField(max_length=1024, null=True, blank=True)

    def __str__(self):
        return self.category_name


class product(models.Model):
    product_name = models.CharField(max_length=30, null=True,blank=True)
    product_price = models.DecimalField(max_digits=10, decimal_places=2)
    Product_description = models.TextField()
    stock = models.IntegerField()
    image = models.ImageField(upload_to='images/', null=True, blank=True)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    category = models.ForeignKey(category, on_delete=models.CASCADE)
    date_added = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
   

    def __str__(self):
        return self.product_name