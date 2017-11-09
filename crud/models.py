from django.db import models


#Students Class to Make Up to the Database
class Student(models.Model):
    first_name = models.CharField(max_length=250)
    middle_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)
    course = models.CharField(max_length=250)
    gender = models.CharField(max_length=250)
    year = models.CharField(max_length=250)



