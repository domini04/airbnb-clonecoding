from django import forms
from django.contrib.admin.widgets import AdminDateWidget, AdminTimeWidget
from .models import Experience

class ExperienceForm(forms.ModelForm):
    class Meta:
        model = Experience
        fields = '__all__'
        widgets = {
            'starts_at': forms.SplitDateTimeWidget(date_attrs={'type': 'date'}, time_attrs={'type': 'time'}),
            'ends_at': forms.SplitDateTimeWidget(date_attrs={'type': 'date'}, time_attrs={'type': 'time'}),
        }