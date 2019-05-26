from django.contrib import admin

from .models import DoctorDetails, PatientSteggedDetails

admin.site.register(DoctorDetails)
admin.site.register(PatientSteggedDetails)

