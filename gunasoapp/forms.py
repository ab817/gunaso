from django import forms
from django.core.exceptions import ValidationError
from django.utils import timezone

from .models import Gunaso


class GunasoForm(forms.ModelForm):
    class Meta:
        model = Gunaso
        fields = ['description', 'incident_date', 'incident_location']
        widgets = {
            'incident_date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'incident_location': forms.Select(attrs={'class': 'form-control'}),
        }

    def clean_description(self):
        description = self.cleaned_data.get('description')
        word_count = len(description.split())

        if word_count > 150:
            raise ValidationError('Description cannot exceed 150 words.')
        return description

    def clean_incident_date(self):
        incident_date = self.cleaned_data['incident_date']
        if incident_date > timezone.now().date():
            raise ValidationError("Incident date cannot be in the future.")
        return incident_date
