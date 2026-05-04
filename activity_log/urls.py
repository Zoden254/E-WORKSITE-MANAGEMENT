from django.urls import path
from . import views

app_name = "activity_log"


urlpatterns = [
    path('departments/', views.DepartmentsList.as_view(), name="departments"),
    path('<str:department_name>/today-activities/', views.today_activities, name='today_activities'),
    path('update-hotel-bill/<int:id>/', views.update_hotel_bill, name='update_hotel_bill'),
    path('update-obligation/<int:id>/', views.update_obligation, name='update_obligation'),
    path('<str:department_name>/pick-date/', views.choose_date, name="pick-date"),
    path('<str:department_name>/<date>/', views.past_activities, name="past-activities"),
]
