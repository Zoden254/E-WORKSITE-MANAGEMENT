from django.db import models
from django.contrib.auth.models import AbstractUser, AbstractBaseUser
from datetime import datetime
from django.db.models import Q
# Create your models here.

class User(AbstractUser):
    #Limited to those who can use the system.
    positions = {
        'OVERALL MANAGER': 'Overall Manager',
        'SITE MANAGER' : 'Site Manager',
        'HOD' : 'Head Of Department',
        'FOREMAN' : 'Foreman',
        'ASSISTANT MANAGER' : 'Assistant Manager',
        'ASSISTANT FOREMAN': 'Assistant Foreman',
        'STOREKEEPER': 'Storekeeper',
        'CASHIER': 'Cashier',
        'OTHERS' : 'Others'
    }

    profile_pic = models.ImageField(blank=True, default='blank_passport.webp')
    position = models.CharField(choices=positions, max_length=50, default='Others')
    ID_number = models.CharField(unique=True, max_length=12)
    phone_no = models.CharField(max_length=13)
    date_registered = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return f'{self.username} - {self.position}'
    
class Department(models.Model):
    department_name = models.CharField(max_length=50)
    HOD = models.OneToOneField(User, on_delete=models.CASCADE, to_field='username')
    job = models.CharField(max_length=255)

    def __str__(self):
        return self.department_name


class Position(models.Model):
    payment_basis_options = {
        'DAILY': 'Daily',
        'WEEKLY' : 'Weekly',
        'MONTHLY': 'Monthly'
    }
    
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    foreman = models.ForeignKey(User, on_delete=models.CASCADE, related_name='foreman', limit_choices_to=Q(position='FOREMAN') | Q(position= 'HOD'))
    assistant_foreman = models.ForeignKey(User, on_delete=models.CASCADE, related_name='assistant_foreman', default=None, null=True, blank=True)
    job_title = models.CharField(max_length=50)
    payment_basis = models.CharField(choices=payment_basis_options, max_length=10)
    payment_amount = models.DecimalField(max_digits=10, decimal_places=2)
    
    def __str__(self):
        return self.job_title

class Employee(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=13)
    passport = models.ImageField(default='blank_passport.webp', blank=True)
    position =models.ForeignKey(Position, on_delete=models.CASCADE)
    date_employed = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'