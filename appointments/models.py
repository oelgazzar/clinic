from django.db import models

from patients.models import Patient

class Appointment(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()
    reason = models.CharField(max_length=255)
    notes = models.TextField(blank=True)

    def __str__(self):
        return f"Appointment for {self.patient.name} on {self.date} at {self.time}"