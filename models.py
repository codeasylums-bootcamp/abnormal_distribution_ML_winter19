from django.db import models
from django.core.validators import RegexValidator

# Create your models here.
class Doctors(models.Model):
    name = models.CharField(max_length=64, null=True)
    address = models.TextField(null=True)
    category = models.CharField(max_length=64, null=False, unique=True)
    locality=models.TextField(null=True)
    def __str__(self):
    	return str(self.name)