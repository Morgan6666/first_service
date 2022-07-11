from django.db import models

class NGSData(models.Model):
    seq = models.CharField(max_length = 255)
    price = models.IntegerField()

