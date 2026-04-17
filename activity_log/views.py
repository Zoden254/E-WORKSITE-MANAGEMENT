from django.shortcuts import render, redirect
from management.models import *
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.views import generic
from django.contrib import messages
from .forms import DailyActivityLogForm
from .models import *
from django.utils import timezone
# Create your views here.

def today_activities(request, department_name):
    activities = DailyActivitie.objects.filter(day=timezone.now().date(), employee__position__department__department_name=department_name)
    dep = Department.objects.get(department_name=department_name)
    form = DailyActivityLogForm(department_name=department_name)
    if request.method == 'POST':
        my_form = DailyActivityLogForm(request.POST)
        if my_form.is_valid():
            my_form.save()
        return HttpResponseRedirect(reverse('activity_log:today_activities', args=(dep,)))
    
    return render(request, 'activities.html', {'activities': activities, 'form': form})

def update_hotel_bill(request, id):
    activity = DailyActivitie.objects.get(id=id)
    dep = activity.employee.position.department.department_name
    try:
        new_hotel_bill = int(request.POST.get('hotel_bill'))
        activity.hotel_bill = new_hotel_bill
        activity.save()
        messages.success(request, f"{activity.employee}'s Hotell Bill Updated Successfully")
    except ValueError:
        messages.error(request, "Only Numbers are allowed")
        return HttpResponseRedirect(reverse('activity_log:today_activities', args=(dep,)))
    return HttpResponseRedirect(reverse('activity_log:today_activities', args=(dep,)))

def update_obligation(request, id):
    activity = DailyActivitie.objects.get(id=id)
    dep = activity.employee.position.department.department_name
    new_obligation = request.POST.get('obligation')
    activity.obligation = new_obligation
    activity.save()
    messages.success(request, f"{activity.employee}'s Obligation Updated Successfully")
    return HttpResponseRedirect(reverse('activity_log:today_activities', args=(dep,)))

class DepartmentsList(generic.ListView):
    model = Department
    context_object_name = 'departments'
    template_name = 'departments.html'