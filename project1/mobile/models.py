from django.db import models

class Mobile(models.Model):
    brand=models.CharField(max_length=30)
    model=models.CharField(max_length=30)
    price=models.PositiveIntegerField()
    year=models.PositiveIntegerField()
    color=models.CharField(max_length=20)
