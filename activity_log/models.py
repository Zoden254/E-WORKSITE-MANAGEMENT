from django.db import models
from management.models import *
from django.db.models import Q
# Create your models here.

class DailyEmployeesActivityLog(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, limit_choices_to=Q(position__payment_basis='DAILY'))
    unpaid_days = models.PositiveIntegerField(default=0)
    hotel_bill = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    obligations = models.TextField(max_length=1000, blank=True, null=True)
    amount_paid = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    balance = models.DecimalField(max_digits=10, decimal_places=2)


class WeeklyEmployeesActivityLog(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, limit_choices_to=Q(position__payment_basis='WEEKLY'))
    unpaid_weeks = models.PositiveIntegerField(default=0)
    hotel_bill = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    obligations = models.TextField(max_length=1000, blank=True, null=True)
    amount_paid = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    balance = models.DecimalField(max_digits=10, decimal_places=2)
    

class MonthlyEmployeesActivityLog(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, limit_choices_to=Q(position__payment_basis='MONTHLY'))
    unpaid_months = models.PositiveIntegerField(default=0)
    hotel_bill = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    obligations = models.TextField(max_length=1000, blank=True, null=True)
    amount_paid = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    balance = models.DecimalField(max_digits=10, decimal_places=2)
    