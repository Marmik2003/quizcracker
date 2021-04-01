from django.db import models

# Create your models here.


# class Student(models.Model):
#     user = models.OneToOneField('user.User', on_delete=models.CASCADE, primary_key=True)
#     tests = models.ManyToManyField('teacher.Test', through='TestTaken')


class TestTaken(models.Model):
    student = models.ForeignKey('user.User', on_delete=models.SET_NULL, null=True)
    test = models.ForeignKey('teacher.Test', on_delete=models.CASCADE)
    points = models.FloatField()


class StudentResponse(models.Model):
    student = models.ForeignKey('user.User', on_delete=models.CASCADE)
    answer = models.ForeignKey('teacher.Option', on_delete=models.CASCADE)
