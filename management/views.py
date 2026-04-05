from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from .forms import *
from activity_log.models import *
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
    

def activities(request):
    return render(request, 'activities.html')

def activitybasis(request, basis):
    if basis == 'daily':
        form = DailyActivityLogForm
        activitylog = DailyEmployeesActivityLog.objects.all()

        return render(request, 'activitybasis.html', {'activity_log': activitylog, 'form': form})
    elif basis == 'weekly':
        activitylog = WeeklyEmployeesActivityLog.objects.all()

        return render(request, 'activitybasis.html', {'activity_log': activitylog})
    elif basis == 'monthly':
        activitylog = MonthlyEmployeesActivityLog.objects.all()

        return render(request, 'activitybasis.html', {'activity_log': activitylog})
    else:
        return redirect('management:activities')