import csv
from django.core.management.base import BaseCommand
from gunasoapp.models import Gunaso

class Command(BaseCommand):
    help = 'Load branches from CSV file'

    def handle(self, *args, **kwargs):
        with open('branches.csv', mode='r') as file:
            reader = csv.reader(file)
            branches = [row[0] for row in reader]

        # Assuming you want to store these in a separate model or use directly
        # For now, let's just print them
        print("Branches loaded:", branches)
