from django.db import models

class Gunaso(models.Model):
    description = models.TextField()
    incident_date = models.DateField()
    incident_location = models.CharField(max_length=255)
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Incident on {self.incident_date} at {self.incident_location}"
