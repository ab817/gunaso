from django.db import models

class Gunaso(models.Model):
    description = models.TextField()
    incident_date = models.DateField()
    RATINGS = (('1 ', 1), ('2 ', 2),
               ('3 ', 3), ('4 ', 4), ('5 ', 5))
    incident_location = models.CharField(max_length=40, choices=RATINGS)
    #incident_location = models.CharField(max_length=255)
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Description of {self.incident_date} at {self.description}"
