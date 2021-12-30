from django.db import models

# Create your models here.


class Destination(models.Model):
    
    name =  models.CharField(max_length=100)
    img  = models.ImageField(upload_to ='pics')
    disc = models.TextField()
    price = models.IntegerField()
    offer = models.BooleanField(default=False)


class Subscriber_information(models.Model):
    name = models.TextField(max_length=30)
    email = models.EmailField(max_length=30)
    
