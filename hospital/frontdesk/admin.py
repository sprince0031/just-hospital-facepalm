from django.contrib import admin

from .models import DoctorDetails, PatientSteggedDetails, AppointmentDetails

admin.site.register(DoctorDetails)
admin.site.register(PatientSteggedDetails)
admin.site.register(AppointmentDetails)

