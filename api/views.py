from django.shortcuts import render
from .serializers import *
from rest_framework import generics
from management.models import *

# Create your views here.

class UsersList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class DepartmentList(generics.ListAPIView):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer

class PositionsList(generics.ListAPIView):
    queryset = Position.objects.all()
    serializer_class = PositionSerializer

class EmployeesList(generics.ListCreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    

class EmployeeDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

class DailyActivitiesList(generics.ListCreateAPIView):
    queryset = DailyActivitie.objects.all()
    serializer_class = DailyActivitiesSerializer

class ActivityDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = DailyActivitie.objects.all()
    serializer_class = DailyActivitiesSerializer