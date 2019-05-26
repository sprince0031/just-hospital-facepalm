from django.shortcuts import get_object_or_404, render
# from django.http import HttpResponse

from .models import DoctorDetails

from .forms import PatientDetailsForm

def index(request): 
    doctor_list = DoctorDetails.objects.order_by('-doctor_availability')
    context = {'doctor_list': doctor_list}
    return render(request, 'frontdesk/home.html', context)

def doctorDetails(request, id):

    doctor = DoctorDetails.objects.get(id=id)

    form = PatientDetailsForm(request.POST or None)
    
    if form.is_valid():
        
        form.save()

    
    context = {'doctor': doctor, 'form': form}
    

    '''
    form = PatientDetailsForm(request.POST or None)
    if form.is_valid():
        form.patient_name = form.cleaned_data['patient_name']
        # form.patient_new = form.cleaned_data['patient_new']
        # form.patient_state = form.cleaned_data['patient_state']
        form.save()
    
    '''

    return render(request, 'frontdesk/doctorDetails.html', context)

def doctorBusy(request, id):
    busyDoctor = DoctorDetails.objects.get(id=id)
    return render(request, 'frontdesk/busyDoctor.html', {'busyDoctor': busyDoctor})