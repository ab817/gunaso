from django.db import models
import csv
import os

def get_branch_choices():
    """ Load branches from CSV file and return as choices """
    branches = []
    csv_path = os.path.join(os.path.dirname(__file__), 'branches.csv')
    try:
        with open(csv_path, mode='r', newline='') as file:
            reader = csv.reader(file)
            for row in reader:
                if row:  # Skip empty rows
                    branch_name = row[0].strip()
                    if branch_name:  # Ensure no empty names
                        branches.append((branch_name, branch_name))
    except FileNotFoundError:
        print(f"CSV file at {csv_path} not found.")
    except Exception as e:
        print(f"An error occurred while loading branches: {e}")
    return branches

class Gunaso(models.Model):
    description = models.TextField()
    incident_date = models.DateField()
    incident_location = models.CharField(max_length=255, choices=get_branch_choices())
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Description of {self.incident_date} at {self.description}"
