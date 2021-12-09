from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.shortcuts import render
from django.utils import timezone

# Create your models here.


class studentgriev(models.Model):
    ch = (
         ("Solved","Solved"),("Pending","Pending"),("Not Solved","Not Solved")
     )
    
    #user = models.ForeignKey(User,on_delete=models.CASCADE,default=1,null=True,blank=True)
    name = models.CharField(max_length=30,default='',null=False)
    contactnum = models.IntegerField(default='',null=False)
    email = models.EmailField(max_length=50,default='',null=False)
    grievance = models.TextField(default='',null=False)
    date_time = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=100,choices=ch,default='')
    
    


    def __str__(self):
        return self.name + " "

class facgrieve(models.Model):
    solution = models.TextField(default='',null=False) 


    def __str__(self):
        return self.solution + " "

class contactus(models.Model):
    ctname = models.CharField(max_length=30,default='',null=False)
    ctemail = models.EmailField(max_length=20,default='',null=False)
    ctsubject = models.CharField(max_length=30,default='',null=False)
    ctmessage = models.TextField(default='',null=False)



