from django.db import models

# Create your models here.

class Department(models.Model):
    code = models.IntegerField()
    department = models.CharField(max_length=100)
    
class Position(models.Model):
    position = models.CharField(max_length=100)
    
class Employee(models.Model):
    GENDER = [
        ("M", "male"),
        ("F", "female"),
        ("L", "lgbt+")
	]
    
    f_name = models.CharField(max_length=100)
    l_name = models.CharField(max_length=100)
    age = models.IntegerField()
    gender = models.CharField(max_length=100, choices=GENDER)
    phone = models.IntegerField()
    department = models.ForeignKey(Department, on_delete=models.CASCADE, default=1)
    position = models.ForeignKey(Position, on_delete=models.CASCADE, default=1)
    salary = models.IntegerField(default=0)
    date_start = models.DateTimeField()