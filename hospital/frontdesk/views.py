from django.shortcuts import get_object_or_404, render
# from django.http import HttpResponse

from .models import DoctorDetails

from .forms import PatientDetailsForm, AppointmentDetailsForm

def index(request): 
    doctor_list = DoctorDetails.objects.order_by('-doctor_availability')
    context = {'doctor_list': doctor_list}
    return render(request, 'frontdesk/home.html', context)

def doctorDetails(request, id):

    doctor = DoctorDetails.objects.get(id=id)

    form = PatientDetailsForm(request.POST or None)
    
    if form.is_valid():
        
        form.save()
    form_1 = AppointmentDetailsForm(request.POST or None)
    if form_1.is_valid():
        form_1.save()
    
    context = {'doctor': doctor, 'form': form, 'form_1': form_1}

    return render(request, 'frontdesk/doctorDetails.html', context)

def doctorBusy(request, id):
    busyDoctor = DoctorDetails.objects.get(id=id)
    return render(request, 'frontdesk/busyDoctor.html', {'busyDoctor': busyDoctor})