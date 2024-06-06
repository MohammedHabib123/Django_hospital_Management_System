from django.db import models

# Create your models here.
class PatientHistory(models.Model):
    PatientName = models.CharField(max_length=70)
    Age=models.CharField(max_length=5)
    BloodPressure = models.CharField(max_length=20)
    BloodSugar = models.CharField(max_length=20)
    Diagnosis = models.TextField(default='Diagnosis')
    Medications = models.TextField(default='Medications')
    Notes = models.TextField(default='Notes')
    RaysAndAnalysis = models.ImageField(upload_to='photos/%y/%m/%d')


    def __str__(self):
        return self.PatientName