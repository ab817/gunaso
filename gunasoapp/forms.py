from django import forms
from .models import Gunaso
import csv
import os


class GunasoForm(forms.ModelForm):
    class Meta:
        model = Gunaso
        fields = ['description', 'incident_date', 'incident_location']
        widgets = {
            'incident_date': forms.DateInput(attrs={'type': 'date'}),
        }

    def __init__(self, *args, **kwargs):
        super(GunasoForm, self).__init__(*args, **kwargs)
        branch_choices = self.get_branches()
        self.fields['incident_location'].choices = branch_choices

        # Set the first branch as the default if there are any branches
        if branch_choices:
            self.initial['incident_location'] = branch_choices[0][0]  # Correct way to set the initial value

    def get_branches(self):
        """ Load branches from CSV file and return as choices """
        branches = []
        csv_path = os.path.join(os.path.dirname(__file__), 'branches.csv')  # Adjust path if needed
        try:
            with open(csv_path, mode='r') as file:
                reader = csv.reader(file)
                branches = [(row[0], row[0]) for row in reader]  # (value, display)
        except FileNotFoundError:
            print(f"CSV file at {csv_path} not found.")
        except Exception as e:
            print(f"An error occurred while loading branches: {e}")
        return branches
