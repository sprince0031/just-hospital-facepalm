# import datetime

from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _
from frontdesk.models import PatientSteggedDetails


class PatientDetailsForm(forms.ModelForm):
    class Meta:
        model = PatientSteggedDetails
        fields = ["patient_name", "patient_new", "patient_state", "patient_age", "patient_DOB", "reason_for_consultation", "appointment_date_time"]

# class AppointmentDetailsForm(forms.ModelForm):
#     class Meta:
#         model = AppointmentDetails
#         fields = ["reason_for_consultation", "appointment_date", "appointment_time"]