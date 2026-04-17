from django.shortcuts import render
from management.models import *
from .forms import DailyActivityLogForm
from .models import *
# Create your views here.



def today_activities(request):
    form = DailyActivityLogForm
    return render(request, 'activities.html', {'form': form})