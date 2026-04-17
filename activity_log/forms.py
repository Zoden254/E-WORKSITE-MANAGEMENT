from django.forms import ModelForm
from .models import DailyActivitie



class DailyActivityLogForm(ModelForm):
    class Meta:
        model = DailyActivitie
        fields = '__all__'

