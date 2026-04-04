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