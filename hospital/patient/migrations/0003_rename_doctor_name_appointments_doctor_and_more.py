# Generated by Django 4.2.1 on 2023-05-26 00:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('patient', '0002_rename_doctor_appointments_doctor_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='appointments',
            old_name='Doctor_name',
            new_name='Doctor',
        ),
        migrations.RenameField(
            model_name='appointments',
            old_name='Patient_name',
            new_name='Patient',
        ),
    ]