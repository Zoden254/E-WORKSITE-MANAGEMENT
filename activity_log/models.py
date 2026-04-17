from django.db import models
from management.models import *
from django.db.models import Q
from datetime import datetime

# Create your models here.


class DailyActivitie(models.Model):
    day = models.DateField(default=datetime.now)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    obligation = models.TextField()
    hotel_bill = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    present = models.BooleanField(default=False)
    attendance_fraction = models.CharField(max_length=10, blank=True)
    balance = models.DecimalField(max_digits=10, decimal_places=2)



