from django.db import models
from django.db.models import Model
from django.contrib.auth.models import User
import datetime
from datetime import *
# Create your models here.

class Donor(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    contact = models.CharField(max_length=15,null=True)
    address = models.CharField(max_length=300,null=True)
    userpic = models.FileField(null=True)
    regdate = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.user.username

class Volunteer(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    contact = models.CharField(max_length=15,null=True)
    address = models.CharField(max_length=300,null=True)
    userpic = models.FileField(null=True)
    picid= models.FileField(null=True)
    aboutme=models.CharField(max_length=300,null=True)
    stat = models.CharField(max_length=50,null=True)
    regdate = models.DateTimeField(auto_now_add=True,blank=True)
    adminremark=models.CharField(max_length=300,null=True)
    updationdate=models.DateField(null=True)
    def __str__(self):
        return self.user.username

class DonationArea(models.Model):
    areaname = models.CharField(max_length=100,null=True)
    description = models.CharField(max_length=300,null=True)
    creationdate = models.DateTimeField(auto_now_add=True,blank=True)
    def __str__(self):
        return self.areaname

class Donation(models.Model):
    donor = models.ForeignKey(Donor,on_delete=models.CASCADE)
    donationname = models.CharField(max_length=100,null=True)
    donationpic = models.FileField(null=True)
    collectionloc=models.CharField(max_length=100,null=True)
    description = models.CharField(max_length=300,null=True)
    stat = models.CharField(max_length=50,null=True)
    donationdate=models.DateTimeField(auto_now_add=True,blank=True)
    adminremark=models.CharField(max_length=300,null=True)
    updationdate = models.DateTimeField(auto_now_add=True,blank=True)
    volunteer=models.ForeignKey(Volunteer,on_delete=models.CASCADE,null=True)
    donationarea=models.ForeignKey(DonationArea,on_delete=models.CASCADE,null=True)
    volunteerremark=models.CharField(max_length=300,null=True)
    updatedtime=models.DateTimeField(auto_now_add=True,blank=True,null=True)
    deliverypic=models.FileField(null=True)
    def __str__(self):
        return self.donationname

# class Gallery(models.Model):
#     donation = models.ForeignKey(Donation,on_delete=models.CASCADE)
#     deliverypic=models.FileField(null=True)
#     creationdate=models.DateTimeField(auto_now_add=True)
#     def __str__(self):
#         return self.id
