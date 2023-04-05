from django.db import models


class Product(models.Model):
    pid = models.IntegerField(primary_key=True)
    pname = models.CharField(max_length=50)
    stock = models.IntegerField()
    mrp = models.IntegerField()

    def __str__(self) -> str:
        return self.pname


class Customer(models.Model):
    cu_id = models.AutoField(primary_key=True,)
    c_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    mobile = models.IntegerField(max_length=12)
    email = models.EmailField()
    address = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.name


class Order(models.Model):
    id = models.OneToOneField(Customer, on_delete=models.CASCADE, primary_key=True)
    address = models.CharField(max_length=100)
    amount = models.PositiveIntegerField()
    date = models.DateField()

    def __str__(self) -> int:
        return self.id


class OrderDetails(models.Model):
    id = models.OneToOneField(Order, on_delete=models.CASCADE, primary_key=True)
    order_id = models.CharField(max_length=100)
    price = models.IntegerField()
    quantity = models.IntegerField()

    def __str__(self) -> int:
        return self.id
