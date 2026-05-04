from django.urls import path
from . import views

app_name = 'api'

urlpatterns = [
    path('users/', views.UsersList.as_view(), name="users-api"),
    path('departments/', views.DepartmentList.as_view(), name='deps-api'),
    path('positions/', views.PositionsList.as_view()),
    path('employees/', views.EmployeesList.as_view()),
    path('employees/<int:pk>/', views.EmployeeDetails.as_view()),
    path('daily-activities/', views.DailyActivitiesList.as_view()),
    path('daily-activities/<int:pk>/', views.ActivityDetail.as_view()),
]
