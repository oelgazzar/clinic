from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required

from .models import Patient
from .forms import PatientForm

@login_required
def patient_list(request):
    q = request.GET.get('q')
    if q:
        patients = Patient.objects.filter(name__icontains=q)
    else:
        patients = Patient.objects.all()
    return render(request, 'patient_list.html', {'patients': patients})

@login_required
def new_patient(request):
    if request.method == 'POST':
        form = PatientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('patient_list')
    else:
       form = PatientForm()
    return render(request, 'patient_form.html',{'form': form})

@login_required
def patient_details(request, patient_id):
    patient = get_object_or_404(Patient, id=patient_id)
    return render(request, 'patient_details.html', {'patient': patient})

@login_required
def edit_patient(request, patient_id):
    patient = get_object_or_404(Patient, id=patient_id)

    if request.method == 'POST':
        form = PatientForm(request.POST, instance=patient)
        if form.is_valid():
            form.save()
            return redirect('patient_details', patient_id=patient.id)
    else:
        form = PatientForm(instance=patient)
        
    return render(request, 'patient_form.html', {'form': form})

@login_required
def delete_patient(request, patient_id):
    patient = get_object_or_404(Patient, id=patient_id)

    if request.method == 'POST':
        patient.delete()
        return redirect('patient_list')

    return render(request, 'delete_patient.html', {'patient': patient})