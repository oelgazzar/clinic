from django.shortcuts import get_object_or_404, redirect, render

from .models import Patient
from .forms import PatientForm

def patient_list(request):
    q = request.GET.get('q')
    if q:
        patients = Patient.objects.filter(name__icontains=q)
    else:
        patients = Patient.objects.all()
    return render(request, 'patient_list.html', {'patients': patients})

def new_patient(request):
    if request.method == 'POST':
        form = PatientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('patient_list')
    else:
       form = PatientForm()
    return render(request, 'patient_form.html',{'form': form, 'submit_button_text': 'Create Patient'})

def patient_details(request, patient_id):
    patient = get_object_or_404(Patient, id=patient_id)
    return render(request, 'patient_details.html', {'patient': patient})


def edit_patient(request, patient_id):
    patient = get_object_or_404(Patient, id=patient_id)

    if request.method == 'POST':
        form = PatientForm(request.POST, instance=patient)
        if form.is_valid():
            form.save()
            return redirect('patient_details', patient_id=patient.id)
        
    return render(request, 'patient_form.html', {'form': form, 'submit_button_text': 'Update Patient'})

def delete_patient(request, patient_id):
    patient = get_object_or_404(Patient, id=patient_id)

    if request.method == 'POST':
        patient.delete()
        return redirect('patient_list')

    return render(request, 'delete_patient.html', {'patient': patient})