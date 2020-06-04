from django.db import models

class Users(models.Model):
    studentName = models.CharField(max_length=15)

    def __str__(self):
        return self.studentName


class Chapter(models.Model):
    testName = models.CharField(max_length=30)
    paperUrl = models.CharField(max_length=200)

    def __str__(self):
        return self.testName


class Marks(models.Model):
    name = models.ForeignKey(Users, on_delete=models.CASCADE)
    test = models.ForeignKey(Chapter,on_delete=models.CASCADE)
    marks = models.CharField(max_length=10)
    remarks = models.CharField(max_length=100)