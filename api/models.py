from django.db import models
from django.contrib.auth.models import User


class Product(models.Model):
    pid = models.IntegerField(primary_key=True)
    pname = models.CharField(max_length=50)
    stock = models.IntegerField()
    mrp = models.IntegerField()

    def __str__(self) -> str:
        return self.pname


class Customer(models.Model):
    customer_id = models.OneToOneField(User, on_delete= models.CASCADE)
    customer_name = models.CharField(max_length=50)
    customer_mobile = models.IntegerField(max_length=12)
    customer_email = models.EmailField()
    customer_address = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.name


class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    date_ordered = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False)

    def __str__(self) -> int:
        return self.id


class OrderDetails(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    total = quantity*product.mrp

    def __str__(self) -> int:
        return self.id
