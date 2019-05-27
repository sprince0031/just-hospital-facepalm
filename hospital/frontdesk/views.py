from django.shortcuts import get_object_or_404, render
# from django.http import HttpResponse

# To localise datetime.now() from UTC
from datetime import datetime, timedelta
import pytz
from pytz import timezone
localZone = timezone('Asia/Kolkata')

from .models import DoctorDetails, PatientSteggedDetails

from .forms import PatientDetailsForm

from background_task import background

# Background task for checking the status of doctor in or out
@background(schedule=10)
def doctorScheduling():
    doctor_list = DoctorDetails.objects.all()
    for doctor in doctor_list:
        localTime = localZone.localize(datetime.now())
        localTimeNow = localTime.time()
        doctorInTime1 = doctor.doctor_shift_slot1_from
        doctorOutTime1 = doctor.doctor_shift_slot1_to
        doctorInTime2 = doctor.doctor_shift_slot2_from
        doctorOutTime2 = doctor.doctor_shift_slot2_to

        if ((localTimeNow > doctorInTime1 and localTimeNow < doctorOutTime1) or (localTimeNow > doctorInTime2 and localTimeNow < doctorOutTime2)):
            # print(True)
            doctor.doctor_availability = True
            doctor.save()
        else:
            # print(False)
            doctor.doctor_availability = False
            doctor.save()
    return 0

# Background task to change state of doctor availability to "busy" on start of appointment
@background(schedule=60)
def setBusyOnAppointmentStart(doctorId):
    doctor = DoctorDetails.objects.get(id=doctorId)
    doctor.doctor_availability = False
    doctor.save()
    return 0

# Background task to change state of doctor availability to "available" on completion of appointment
@background(schedule=60)
def setAvailableOnAppointmentEnd(doctorId):
    doctor = DoctorDetails.objects.get(id=doctorId)
    doctor.doctor_availability = True
    doctor.save()
    return 0

# handle the calculation of time till appointment commence datetime by converting the datetime to seconds using datetime.timedelta()
def getBusy(patientDetails, doctor):
    appointmentFormTime = patientDetails.appointment_form_submission_date_time
    scheduledTime = patientDetails.appointment_date_time
    timeToAppointment = int((scheduledTime - appointmentFormTime).total_seconds()) # IMPORTANT: Background task scheduler has to get arguments in int only and not float
    setBusyOnAppointmentStart(doctor.id, schedule=timeToAppointment) # Pass schedule offset in seconds to background task
    patientCondition = patientDetails.patient_state
    sessionTime = 0
    if patientCondition == 'N':
        sessionTime = 20
    elif patientCondition == 'U':
        sessionTime = 30
    else:
        return 0
    timeTillSwitch = int(timedelta(minutes=(sessionTime+2)).total_seconds() + timeToAppointment)
    setAvailableOnAppointmentEnd(doctor.id, schedule=timeTillSwitch)
    return 0


def index(request): 
    doctor_list = DoctorDetails.objects.order_by('-doctor_availability')
    doctorScheduling()
    context = {'doctor_list': doctor_list}
    return render(request, 'frontdesk/home.html', context)

def doctorDetails(request, id):

    doctor = DoctorDetails.objects.get(id=id)

    form = PatientDetailsForm(request.POST or None)
    
    if form.is_valid():
        form.save()
        # get latest record of patientdetails saved to db based on form submission auto timestamp
        patientDetails = PatientSteggedDetails.objects.latest('appointment_form_submission_date_time')
        getBusy(patientDetails, doctor)

    # form_1 = AppointmentDetailsForm(request.POST or None)
    # if form_1.is_valid():
    #     form_1.save()
    
    context = {'doctor': doctor, 'form': form}

    return render(request, 'frontdesk/doctorDetails.html', context)

def doctorBusy(request, id):
    busyDoctor = DoctorDetails.objects.get(id=id)
    return render(request, 'frontdesk/busyDoctor.html', {'busyDoctor': busyDoctor})