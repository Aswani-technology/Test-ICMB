from pyexpat import model
from django.db import models

# Create your models here.
class SalesTeam(models.Model):
    firstname=models.CharField(max_length=50)
    lastname=models.CharField(max_length=50)
    email=models.EmailField(max_length=50)
    phone=models.IntegerField()
    company=models.CharField(max_length=50)
    hear_about_us=models.CharField(max_length=50)
    comment=models.CharField(max_length=100)
