from django.forms import ModelForm
from management.models import Employee
from activity_log.models import *

class RegisterEmployeeForm(ModelForm):
    class Meta:
        model = Employee
        fields = ('first_name', 'last_name', 'phone_number', 'position', 'passport')

class DailyActivityLogForm(ModelForm):
    class Meta:
        model = DailyEmployeesActivityLog
        fields = '__all__'

