from django.forms import ModelForm
from management.models import Employee

class RegisterEmployeeForm(ModelForm):
    class Meta:
        model = Employee
        fields = ('first_name', 'last_name', 'phone_number', 'position', 'passport')

        