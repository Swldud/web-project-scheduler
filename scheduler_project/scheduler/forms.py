from django import forms
from .models import Schedule


class ScheduleForm(forms.ModelForm):
    title = forms.CharField(max_length=30)
    time = forms.TimeField()
    date = forms.DateField()
    place = forms.CharField(max_length=20)
    memo = forms.CharField(max_length=200)

    class Meta:
        model = Schedule
        fields = '__all__'