from django.db import models


class student(models.Model):
    name=models.CharField(max_length=20)
    age=models.IntegerField(default=0)
    address=models.TextField()


