from django.shortcuts import get_object_or_404, render
# from django.http import HttpResponse

from .models import DoctorDetails

def index(request): 
    doctor_list = DoctorDetails.objects.order_by('-doctor_availability')
    context = {'doctor_list': doctor_list}
    return render(request, 'frontdesk/home.html', context)

def doctorDetails(request, doctor_name):
    doctor = DoctorDetails.objects.get(doctor_name=doctor_name)
    return render(request, 'frontdesk/doctorDetails.html', {'doctor': doctor})
