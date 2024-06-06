from django.db import models

# Create your models here.

class Appointments(models.Model):
    Patient = models.CharField(max_length=70)
    Date = models.DateField()
    Time = models.TimeField()
    Doctor = models.CharField(max_length=70)

    def __str__(self):
        return self.Patient