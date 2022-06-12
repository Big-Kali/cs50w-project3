
from email.policy import default
from django.db import models

# Create your models here.


class menu(models.Model):
    id = models.AutoField(primary_key=True)
    type_food = models.CharField(max_length=50)
    price1 = models.IntegerField()
    price2 = models.IntegerField()
    image = models.ImageField(default='null', upload_to="imagenes")
    
class toppings(models.Model):
    id = models.AutoField(primary_key=True)
    toppins = models.CharField(max_length=250)
    
class subs(models.Model):
    id = models.AutoField(primary_key=True)
    typesubs = models.CharField(max_length=250)
    pricesubs = models.IntegerField()
    priceSsubs = models.IntegerField()

class pasta(models.Model):
    id = models.AutoField(primary_key=True)  
    typepasta = models.CharField(max_length=100)
    pricepasta = models.IntegerField()
    
class salads(models.Model):
    id = models.AutoField(primary_key=True)  
    typesalads = models.CharField(max_length=100)
    pricesalads = models.IntegerField()
    
class Dinner(models.Model):
    id = models.AutoField(primary_key=True)  
    type_dinner = models.CharField(max_length=250)
    price_dinner = models.IntegerField()
    
    
class Pedido(models.Model):
    id = models.AutoField(primary_key=True)  
    user = models.CharField(max_length=50, default="None")
    cantidad = models.IntegerField(default=0)
    categoria = models.CharField(max_length=64)
    precio = models.IntegerField()

   
    
