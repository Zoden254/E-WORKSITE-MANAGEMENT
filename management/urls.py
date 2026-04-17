from django.urls import path
from . import views

app_name = 'management'

urlpatterns = [
    path('', views.home, name='home'),
    path('register_employee/', views.register_employee, name='register_employee'),
    path('employees/', views.employees, name='employees'),
]

