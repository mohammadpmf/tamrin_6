from django.db import models


class Student(models.Model):
    name = models.CharField(max_length=30)
    father_name = models.CharField(max_length=30)
    color = models.CharField(max_length=30)
    food = models.CharField(max_length=30)

    def __str__(self):
        return self.name