from django.db import models


class Student(models.Model):
    name = models.CharField(max_length=100,null=True, blank=True)
    age = models.IntegerField(null=True, blank=True)
    place = models.CharField(max_length=100,null=True, blank=True)
    mobile = models.CharField(max_length=100,null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    course = models.CharField(max_length=100,null=True, blank=True)