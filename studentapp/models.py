from django.db import models

class Course(models.Model):
    coursename=models.CharField(max_length=100)

    def __str__(self):
        return self.coursename
class Student(models.Model):
    studentname=models.CharField(max_length=100)
    courses=models.ManyToManyField(Course,related_name='students')
    def __str__(self):
        return self.studentname

# Create your models here.
