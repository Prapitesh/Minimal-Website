from django import forms
from .models import Patient

class PatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = ['name', 'age', 'gender', 'contact_number', 'aadhar_or_kyc', 'medical_concern', 'treatment_advice']
        