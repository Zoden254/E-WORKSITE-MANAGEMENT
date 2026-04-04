from django.contrib import admin
from .models import *


# Register your models here.
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('department_name', 'HOD')
    search_fields = ('department_name', 'HOD')

class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'position', 'date_registered')
    search_fields = ('username')


admin.site.register([Department, User, Position, Employee])