from django.shortcuts import get_object_or_404, render
# from django.http import HttpResponse
from django.utils import timezone
from django.utils.timezone import activate
from hospital import settings
activate(settings.TIME_ZONE)

from .models import DoctorDetails, PatientSteggedDetails

from .forms import PatientDetailsForm

from .tasks import doctorScheduling

def getBusy(doc, patient_state='normal', appointment_date=timezone.now().date(), appointment_time=timezone.now().time()):
    if appointment_date > timezone.now().date():
        # @Superman: Remove this if and unindent the following two lines to see the busy flag chaning on submitting appointment form. Incomplete for now (if logic to be added to check for checking if appointment fixed is in the future or present)
        doc.doctor_availability = False
        doc.save()
    # if patient_state == 'normal':
    return 0


def index(request): 
    doctor_list = DoctorDetails.objects.order_by('-doctor_availability')
    doctorScheduling(repeat=10, repeat_until=None)
    context = {'doctor_list': doctor_list}
    return render(request, 'frontdesk/home.html', context)

def doctorDetails(request, id):

    doctor = DoctorDetails.objects.get(id=id)

    form = PatientDetailsForm(request.POST or None)
    
    if form.is_valid():
        getBusy(doctor, form.fields['patient_state'], form.fields['appointment_date'], form.fields['appointment_time'])
        form.save()
    # form_1 = AppointmentDetailsForm(request.POST or None)
    # if form_1.is_valid():
    #     form_1.save()
    
    context = {'doctor': doctor, 'form': form}

    return render(request, 'frontdesk/doctorDetails.html', context)

def doctorBusy(request, id):
    busyDoctor = DoctorDetails.objects.get(id=id)
    return render(request, 'frontdesk/busyDoctor.html', {'busyDoctor': busyDoctor})