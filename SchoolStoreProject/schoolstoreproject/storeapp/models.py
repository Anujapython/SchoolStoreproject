from django.db import models

# Create your models here.
class logins(models.Model):
    username=models.CharField(max_length=250)
    password=models.CharField(max_length=250)

class register(models.Model):
    username = models.CharField(max_length=250)
    password = models.CharField(max_length=250)
    password1 = models.CharField(max_length=250)

class Department(models.Model):
    name=models.CharField(max_length=50)
    def __str__(self):
        return self.name

class Course(models.Model):
    name=models.CharField(max_length=50)
    department=models.ForeignKey(Department, on_delete=models.CASCADE)
    def __str__(self):
        return self.name
class Person(models.Model):
    department = models.ForeignKey(Department, on_delete=models.SET_NULL, blank=True, null=True)
    course = models.ForeignKey(Course, on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return self.name

