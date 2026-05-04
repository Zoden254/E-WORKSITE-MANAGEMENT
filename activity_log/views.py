from django.shortcuts import render, redirect
from management.models import *
from django.core.paginator import Paginator
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.views import generic
from django.db.models import Count
from django.contrib import messages
from .forms import DailyActivityLogForm
from .models import *
from django.utils import timezone
# Create your views here.

def today_activities(request, department_name):
    selected_day = timezone.now().date()
    activities = DailyActivitie.objects.filter(day=selected_day, employee__position__department__department_name=department_name)
    activities = Paginator(activities, 10)
    page_number = request.GET.get('page')
    activities = activities.get_page(page_number)
    dep = Department.objects.get(department_name=department_name)
    dep_name = dep.department_name
    form = DailyActivityLogForm(department_name=department_name)
    if request.method == 'POST':
        my_form = DailyActivityLogForm(request.POST)
        if my_form.is_valid():
            my_form.save()
        return HttpResponseRedirect(reverse('activity_log:today_activities', args=(dep,)))
    
    return render(request, 'activities.html', {'activities': activities, 'form': form, 'selected_day': selected_day, 'dep_name':dep_name})



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

def choose_date(request, department_name):
    dates = DailyActivitie.objects.values_list('day', flat=True).order_by('-day').distinct()
    dep = department_name
    return render(request, 'dates.html', {'dates': dates, 'dep':dep})


def past_activities(request, date, department_name):
    
    activities = DailyActivitie.objects.filter(employee__position__department__department_name=department_name, day=date)
    today = timezone.now().date()
    date = datetime.strptime(date, '%Y-%m-%d').date()
    if date == today:
        form = DailyActivityLogForm(department_name=department_name)
        return HttpResponseRedirect(reverse('activity_log:today_activities', args=(department_name,)))
    return render(request, 'activities.html', {'activities':activities, 'dep_name':department_name, 'selected_day':date, 'today':today})