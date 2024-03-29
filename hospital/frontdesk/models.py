from django.db import models

import datetime
from django.utils import timezone


class DoctorDetails(models.Model):
    doctor_name = models.CharField(max_length=50)
    doctor_availability = models.BooleanField(default=True)
    doctor_specialisation = models.CharField(max_length=200)
    doctor_shift_slot1_from = models.TimeField()
    doctor_shift_slot1_to = models.TimeField()
    doctor_shift_slot2_from = models.TimeField()
    doctor_shift_slot2_to = models.TimeField()
    doctor_sex = models.CharField(max_length=1)
    def __str__(self):
        return self.doctor_name


# class AppointmentDetails(models.Model):
#     # appointment_id = models.CharField(max_length=14, null=True)
#     # reason_for_consultation = models.CharField(max_length=300, null=True)    
#     # appointment_date = models.DateField()
#     # appointment_time = models.TimeField()
#     patient_hash = models.CharField(max_length=64)
#     patient_name = models.CharField(max_length=100)
#     appointment_doctor = models.CharField(max_length=50)
#     # doctor_availability = models.ForeignKey(DoctorDetails, on_delete=models.CASCADE, default=False)
#     def __str__(self):
#         return self.appointment_id

class PatientSteggedDetails(models.Model):
    # patient = models.ForeignKey(DoctorDetails, on_delete=models.CASCADE)
    patient_name = models.CharField(max_length=100)
    # patient_steg = models.ImageField(null=True, blank=True)
    NORMAL = 'N'
    URGENT = 'U'
    EMERGENCY = 'E'
    PATIENT_STATE_CHOICES = [
        (NORMAL, 'normal'),
        (URGENT, 'need urgent attention'),
        (EMERGENCY, 'emergency')
    ]
    patient_state = models.CharField(
        max_length=25,
        choices=PATIENT_STATE_CHOICES,
        default=NORMAL,
    )
    patient_new = models.BooleanField(default=True)
    patient_age = models.IntegerField(null=True)
    patient_DOB = models.DateField(null=True)
    reason_for_consultation = models.CharField(max_length=300, null=True)    
    appointment_date_time = models.DateTimeField(null=True)
    appointment_form_submission_date_time = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.patient_name
    
    def appointment_timestamp(self):
        return self.appointment_date_time >= timezone.now().minute() - datetime.timedelta(min=1)
