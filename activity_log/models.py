from django.db import models
from management.models import *
from django.db.models import Q
# Create your models here.


class DailyEmployeesActivityLog(models.Model):
    date = models.DateTimeField(default=datetime.now)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, limit_choices_to=Q(position__payment_basis='DAILY'), unique_for_date='date')
    unpaid_period = models.PositiveIntegerField(default=0)
    hotel_bill = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    obligations = models.TextField(max_length=1000, blank=True, null=True)
    amount_paid = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    balance = models.DecimalField(max_digits=10, decimal_places=2, default=0, editable=False)
    present_today = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        hotel_bill = self.hotel_bill or 0
        unpaid_period = self.unpaid_period or 0
        amount_paid = self.amount_paid
        self.balance = self.employee.position.payment_amount * unpaid_period - hotel_bill - amount_paid
        super().save(*args, **kwargs)

    def __str__(self):
        return 'DailyActivityLog'

class WeeklyEmployeesActivityLog(models.Model):
    date = models.DateTimeField(default=datetime.now)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, limit_choices_to=Q(position__payment_basis='WEEKLY'))
    unpaid_period = models.PositiveIntegerField(default=0)
    hotel_bill = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    obligations = models.TextField(max_length=1000, blank=True, null=True)
    amount_paid = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    balance = models.DecimalField(max_digits=10, decimal_places=2, default=0, editable=False)
    

    def save(self, *args, **kwargs):
        hotel_bill = self.hotel_bill or 0
        unpaid_period = self.unpaid_period or 0
        amount_paid = self.amount_paid
        self.balance = self.employee.position.payment_amount * unpaid_period - hotel_bill - amount_paid
        super().save(*args, **kwargs)
    
    def __str__(self):
        return 'WeeklyActivityLog'


class MonthlyEmployeesActivityLog(models.Model):
    date = models.DateTimeField(default=datetime.now)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, limit_choices_to=Q(position__payment_basis='MONTHLY'), unique_for_month='date')
    unpaid_period = models.PositiveIntegerField(default=0)
    hotel_bill = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    obligations = models.TextField(max_length=1000, blank=True, null=True)
    amount_paid = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    balance = models.DecimalField(max_digits=10, decimal_places=2, default=0, editable=False)

    def save(self, *args, **kwargs):
        hotel_bill = self.hotel_bill or 0
        unpaid_period = self.unpaid_period or 0
        amount_paid = self.amount_paid
        self.balance = self.employee.position.payment_amount * unpaid_period - hotel_bill - amount_paid
        super().save(*args, **kwargs)
    
    def __str__(self):
        return 'MonthlyActivityLog'

 