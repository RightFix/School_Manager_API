from django.db import models
from .const import GRADES, COURSES
# Create your models here.

class Profile(models.Model):
    reg_no = models.CharField(max_length= 15, unique= True, primary_key= True)
    created_at = models.DateTimeField( auto_now=True)

class Grade(models.Model):
    student  = models.ForeignKey("student.Profile", on_delete=models.CASCADE, related_name = 'grades')
    math= models.CharField( max_length=1, choices =GRADES, default= "")
    english = models.CharField( max_length=1,choices= GRADES, default= "")
    chemistry= models.CharField( max_length=1, choices= GRADES, default= "")
    physics= models.CharField( max_length=1, choices=GRADES, default= "")
    created_at = models.DateTimeField(auto_now=True)