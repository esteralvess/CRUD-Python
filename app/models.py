import email

from django.db import models
from phone_field import PhoneField
from pyexpat import model

# Create your models here.

class  Carro(models.Model):
    modelo = models.CharField(max_length=150)
    marca = models.CharField(max_length=100)
    ano = models.IntegerField ()
