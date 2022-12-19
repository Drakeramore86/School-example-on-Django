from django.db import models
from django.shortcuts import render
from django.contrib.auth.models import User


# Create your models here.
class Teacher(models.Model):
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    age = models.IntegerField()
    about = models.TextField(max_length=1024)

    # class Meta:
    #     ordering = ['surname']

    def __str__(self):
        return self.surname


class Course(models.Model):
    title = models.CharField(max_length=255)
    info = models.TextField(max_length=1024)
    duration_months = models.IntegerField()
    price = models.IntegerField()
    teacher = models.ManyToManyField(Teacher)
    # class Meta:

    def __str__(self):
        return self.title


class Student(models.Model):
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    age = models.IntegerField()
    course = models.ManyToManyField(Course)

    # class Meta:

    def __str__(self):
        return self.surname