from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from .forms import RegisterEmployeeForm
from .models import *

# Create your views here.
def home(request):
    return render(request, 'home.html')

def employees(request):
    employees = Employee.objects.all()
    return render(request, 'employees.html', {'employees': employees})

def register_employee(request):
    if request.method == 'POST':
        form = RegisterEmployeeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('management:employees')

    else:
        form = RegisterEmployeeForm
        return render(request, 'register_employee.html', {'form': form})