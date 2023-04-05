from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('create-customer', views.add_customer, name='add-customer'),
    path('customer', views.get_customer, name ="get-customer"),
    path('customer/<int:pk>', views.get_particular_customer, name ="get-particular-customer"),


]
