from django.db import models
from management.models import *
from django.db.models import Q
from django.utils import timezone

# Create your models here.

class DailyActivitie(models.Model):
    day = models.DateField(default=timezone.now)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, unique_for_date="day")
    obligation = models.TextField(blank=True, null=True)
    hotel_bill = models.DecimalField(max_digits=10, decimal_places=0, default=0)
    present = models.BooleanField(default=False)
    attendance_fraction = models.CharField(max_length=10, blank=True)
    balance = models.DecimalField(max_digits=10, decimal_places=2, default=0, editable=False)

    def save(self, *args, **kwargs):
        salary = self.employee.position.payment_amount
        hotel_bill = self.hotel_bill or 0
        self.balance = salary - hotel_bill
        
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.day} - {self.employee}"