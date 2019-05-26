# import datetime

from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _
from .models import PatientSteggedDetails



# class PatientDetailsForm(forms.ModelForm):
class PatientDetailsForm(forms.ModelForm):
    class Meta:
        model = PatientSteggedDetails
        fields = ["patient_name", "patient_new", "patient_state"]

    # patient_name = forms.CharField(required=True)
    # patient_new = forms.BooleanField(required=True, initial=True)
    # patient_state = forms.MultipleChoiceField(required=True)

    # def clean_renewal_date(self):
    #     data = self.cleaned_data['renewal_date']
        
    #     # Check if a date is not in the past. 
    #     if data < datetime.date.today():
    #         raise ValidationError(_('Invalid date - renewal in past'))
        
    #     return data

    # class PatientDetailsForm(forms.ModelForm):

    #     class Meta:
    #         model = PatientSteggedDetails