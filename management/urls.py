from django.urls import path
from . import views

app_name = 'management'

urlpatterns = [
    path('', views.home, name='home'),
    path('register_employee/', views.register_employee, name='register_employee'),
    path('employees/', views.EmployeesList.as_view(), name='employees'),
    path('login/', views.login_view, name="login"),
    path('logout/', views.logout_view, name="logout"),
]

