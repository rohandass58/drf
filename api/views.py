from django.shortcuts import render
from rest_framework.decorators import api_view

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from .models import Product, Customer, Order, OrderDetails
from .serializers import ProductSerializer, CustomerSerializer, OrderSerializer, OrderDetailSerializer

from rest_framework import serializers
from rest_framework import status


@api_view(['POST'])
def add_customer(request):
    # customer contain the serialized data then the serialized data is get validated and if it is new customer then,
    # the new data is added
    customer = CustomerSerializer(data=request.data)
    # item = ItemSerializer(data=request.data)

    # validating for already existing data
    if Customer.objects.filter(**request.data).exists():
        raise serializers.ValidationError('This data already exists')
    if customer.is_valid():
        customer.save()
        return Response(customer.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def get_customer(request):
    # checking for the parameters from the URL
    # request.get is similar to request.query_params
    if request.query_params:
        customer = Customer.objects.filter(**request.query_params.dict())
    else:
        customer = Customer.objects.all()
    # if there is something in Customer return it,  else --> raise error
    if customer:
        serializer = CustomerSerializer(customer, many=True)
        return Response(serializer.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def get_particular_customer(request, pk):
    # checking for the parameters from the URL
    # request.get is similar to request.query_params
    if request.query_params:
        customer = Customer.objects.filter(**request.query_params.dict())
    else:
        customer = Customer.objects.get(pk=pk)
    # if there is something in Customer return it,  else --> raise error
    if customer:
        serializer = CustomerSerializer(customer, many=True)
        return Response(serializer.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)


# class CustomerAPI(APIView, ):
#     def get(self, request, *args, **kwargs):
#         '''
#         List all the CUSTOMER  for given requested user
#         '''
#         customers = Customer.objects.filter(user=request.user.id)
#         serializer = CustomerSerializer(customers, many=True)
#         return Response(serializer.data, status=status.HTTP_200_OK)
