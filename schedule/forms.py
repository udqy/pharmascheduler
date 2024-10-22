from django import forms
from .models import Schedule

class ScheduleUploadForm(forms.ModelForm):
    class Meta:
        model = Schedule
        fields = ['schedule_file']
