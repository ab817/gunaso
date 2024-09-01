from django import forms
from django.core.exceptions import ValidationError

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
