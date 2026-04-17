from django.forms import ModelForm
from .models import DailyActivitie
from .models import Employee
from django.db.models import Q
from django.utils import timezone



class DailyActivityLogForm(ModelForm):
    class Meta:
        model = DailyActivitie
        fields = ['employee']

    def __init__(self, *args, **kwargs):
        department_name = kwargs.pop('department_name', None)
        super().__init__(*args, **kwargs)

        if department_name:
            today_activities = DailyActivitie.objects.filter(day=timezone.now().date())
            already_in_ids = today_activities.values_list('employee', flat=True)
            self.fields['employee'].queryset = Employee.objects.filter(
                    position__department__department_name=department_name,
                    ).exclude(id__in=already_in_ids)