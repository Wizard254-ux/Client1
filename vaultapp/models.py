from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid
from django.utils import timezone


class User(AbstractUser):

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.username



class clientInfo(models.Model):
    user=models.ForeignKey(User,related_name='clientInformation',on_delete=models.CASCADE)
    full_name=models.CharField(max_length=50,blank=False)
    email=models.EmailField(blank=False)
    mobileNumber=models.CharField(max_length=20,blank=False)
    created = models.DateTimeField(auto_now_add=True)
    subject=models.CharField(max_length=50,blank=False)
    message=models.CharField(max_length=500,blank=False)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user



class propertyInfo(models.Model):
     
    title=models.CharField(max_length=100,blank=False)
    rent=models.FloatField(blank=False,default=0)
    buy=models.FloatField(blank=False)
    location=models.CharField(max_length=100,blank=False)
    type=models.CharField(max_length=100,blank=False,default='')
    bedrooms=models.IntegerField(blank=False,default=0)
    bathrooms=models.IntegerField(blank=False,default=0)
    area=models.FloatField(blank=False,default=0)
    description=models.CharField(max_length=100,blank=False)

    def __str__(self):
        return self.title


class PropertyImage(models.Model):
    property = models.ForeignKey(propertyInfo, related_name='images_read', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='property_images/')

    def __str__(self):
        return f"Image for {self.property.title} "


class PropertyReview(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField(max_length=50)
    message=models.CharField(max_length=500)
    
    def __str__(self):
        return self.name