from django.shortcuts import render, redirect, get_object_or_404
from .models import Patient
from .forms import PatientForm
from openpyxl import Workbook
# Create your views here.
from django.contrib import auth
from .forms import PatientForm
from django.http import HttpResponse
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.http import Http404
def home(request):
    return HttpResponse("Welcome to my Django app!")
def doctor_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('patient_form')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})
def patient_form(request, patient_id=None):
    if patient_id:
        patient = get_object_or_404(Patient, id=patient_id)
    else:
        patient = None

    if request.method == 'POST':
        form = PatientForm(request.POST, instance=patient)
        if form.is_valid():
            form.save()
            return redirect('patient_list')  # Redirect to the list view after saving
    else:
        form = PatientForm(instance=patient)

    return render(request, 'patient_form.html', {'form': form})
def patient_list(request):
    patients = Patient.objects.all()
    print(patients)  # Debugging: Check if patients queryset is correctly populated
    return render(request, 'patient_list.html', {'patients': patients})
def patient_view(request, patient_id):
    try:
        patient = Patient.objects.get(id=patient_id)
    except Patient.DoesNotExist:
        raise Http404("Patient not found")
    return render(request, 'patient_view.html', {'patient': patient})
def export_patient_data(request):
    # Fetch all patient data
    patients = Patient.objects.all()

    # Create an Excel workbook and add data
    wb = Workbook()
    ws = wb.active
    ws.title = "Patients Data"
    ws.append(['Name', 'Age', 'Gender', 'Contact Number', 'Aadhar/KYC', 'Medical Concern', 'Treatment/Advice'])

    for patient in patients:
        ws.append([
            patient.name,
            patient.age,
            patient.gender,
            patient.contact_number,
            patient.aadhar_or_kyc,
            patient.medical_concern,
            patient.treatment_advice
        ])

    # Prepare HTTP response with Excel file
    response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    response['Content-Disposition'] = 'attachment; filename="patients.xlsx"'
    wb.save(response)
    return response
def patient_delete(request, patient_id):
    patient = get_object_or_404(Patient, id=patient_id)
    patient.delete()
    return HttpResponseRedirect(reverse('patient_list'))


def Logout(request):
    auth.logout(request)
    return redirect('/login')