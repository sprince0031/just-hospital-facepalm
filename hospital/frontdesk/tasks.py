from background_task import background
from django.utils import timezone
from django.utils.timezone import activate
from hospital import settings
activate(settings.TIME_ZONE)

from .models import DoctorDetails, AppointmentDetails
@background(schedule=60)
def doctorScheduling():
    doctor_list = DoctorDetails.objects.all()
    for doctor in doctor_list:
        timeNow = timezone.now().time()
        doctorInTime1 = doctor.doctor_shift_slot1_from
        doctorOutTime1 = doctor.doctor_shift_slot1_to
        doctorInTime2 = doctor.doctor_shift_slot2_from
        doctorOutTime2 = doctor.doctor_shift_slot2_to
        print(doctorOutTime2)
        print(timeNow)
        if (timeNow > doctorOutTime2 and timeNow < doctorInTime1) or (timeNow > doctorOutTime1 and timeNow < doctorInTime2):
        # if timeNow > doctorOutTime2:
            print((timeNow > doctorOutTime2 and timeNow < doctorInTime1) or (timeNow > doctorOutTime1 and timeNow < doctorInTime2))
            doctor.doctor_availability = False
            doctor.save()
    return 0
