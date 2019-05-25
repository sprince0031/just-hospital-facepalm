from django.db import models


class DoctorDetails(models.Model):
    doctor_name = models.CharField(max_length=50)
    doctor_availability = models.BooleanField(default=True)
    doctor_specialisation = models.CharField(max_length=200)
    doctor_shift_slot1 = models.IntegerField(default=0)
    doctor_shift_slot2 = models.IntegerField(default=0)
    doctor_sex = models.CharField(max_length=1)
    def __str__(self):
        return self.doctor_name


class AppointmentDetails(models.Model):
    appointment_id = models.CharField(max_length=14)
    appointment_date = models.DateField()
    appointment_time = models.TimeField()
    patient_hash = models.CharField(max_length=64)
    appointment_doctor = models.CharField(max_length=50)
    doctor_availability = models.ForeignKey(DoctorDetails, on_delete=models.CASCADE)
    def __str__(self):
        return self.appointment_id

class PatientSteggedDetails(models.Model):
    patient_steg = models.ImageField()
    patient_new = models.BooleanField(default=False)
    def __str__(self):
        return self.patient_steg