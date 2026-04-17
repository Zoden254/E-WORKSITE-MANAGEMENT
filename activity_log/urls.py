from django.urls import path
from . import views

app_name = "activity_log"


urlpatterns = [
    path('today-activities', views.today_activities, name='today_activities')
]
