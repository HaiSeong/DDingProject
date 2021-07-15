from django.db import models

# Create your models here.

class Call(models.Model):
    stId = models.CharField(max_length=15)
    stnNm = models.CharField(max_length=60)
    busRouteId = models.CharField(max_length=15)
    vehId1 = models.CharField(max_length=15)
