from django import forms
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
