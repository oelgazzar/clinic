from django.db import models

class Patient(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    date_of_birth = models.DateField()

    def __str__(self):
        return self.name
