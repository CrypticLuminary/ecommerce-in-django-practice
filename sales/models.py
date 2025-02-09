from django.db import models
from user.models import Myuser
from product.models import product

class Buyer(models.Model):
    buyer_name = models.ManyToManyField(Myuser)
    buyes_on = models.DateField(auto_now_add=True)

    def __str__(self):  # Fixed syntax
        return ', '.join([user.username for user in self.buyer_name.all()]) or 'No buyers'

class Sales(models.Model):
    product_name = models.ForeignKey(product, on_delete=models.CASCADE, null=True, blank=True)
    buyer = models.ManyToManyField(Buyer)
    quantity = models.IntegerField()
    date_of_purchase = models.DateField(auto_now_add=True)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    payment_method = models.CharField(max_length=20)
    payment_status = models.BooleanField(default=False)

    def __str__(self):  # Fixed to return string
        return str(self.product_name)