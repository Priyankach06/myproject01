from django.db import models

# Create your models here.

class Contact(models.Model):
	name=models.CharField(max_length=30)
	phone=models.IntegerField()
	email=models.EmailField()
	message=models.CharField(max_length=100)