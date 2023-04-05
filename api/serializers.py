from django.db.models import fields
from rest_framework import serializers
from .models import Product, Customer, Order, OrderDetails


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('pid', 'pname', 'stock', 'quantity', 'mrp')


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ('c_id', 'name', 'mobile', 'email', 'address')


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ('id', 'address', 'amount', 'date')


class OrderDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderDetails
        fields = ('id', 'order_id', 'price', 'quantity')
