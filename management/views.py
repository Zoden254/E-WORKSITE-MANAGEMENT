from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from .forms import *
from django.views import generic
from django.db.models import Count
from activity_log.models import *
from .models import *
from django.contrib.auth import authenticate, login, logout

# Create your views here.
def home(request):
    return render(request, 'home.html')


class EmployeesList(generic.ListView):
    model = Employee
    context_object_name = 'employees'
    template_name = "employees.html"
    paginate_by = 6


def register_employee(request):
    if request.method == 'POST':
        form = RegisterEmployeeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('management:employees')

    else:
        form = RegisterEmployeeForm
        return render(request, 'register_employee.html', {'form': form})
    

def login_view(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('management:home')
        
    return render(request, "login.html")

def logout_view(request):
    logout(request)
    return redirect('management:login')