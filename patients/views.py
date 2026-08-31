from django.shortcuts import get_object_or_404, redirect, render

from .models import Patient
from appointments.models import Appointment

def patient_list(request):
    q = request.GET.get('q')
    if q:
        patients = Patient.objects.filter(name__icontains=q)
    else:
        patients = Patient.objects.all()
    return render(request, 'patient_list.html', {'patients': patients})

def new_patient(request):
    ctx = {
        'error': None,
        'submit_button_text': 'Create Patient'
    }

    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        date_of_birth = request.POST.get('date_of_birth')
        print(date_of_birth)
        ctx.update({'name': name, 'phone': phone, 'date_of_birth': date_of_birth})

        if not name or not phone or not date_of_birth:
            ctx.update({'error': "All fields are required."})
        else:
            Patient.objects.create(name=name, phone=phone, date_of_birth=date_of_birth)
            return redirect('patient_list')

    return render(request, 'patient_form.html', ctx)

def patient_details(request, patient_id):
    patient = get_object_or_404(Patient, id=patient_id)
    appointments = Appointment.objects.filter(patient=patient)
    return render(request, 'patient_details.html', {'patient': patient, 'appointments': appointments})


def edit_patient(request, patient_id):
    patient = get_object_or_404(Patient, id=patient_id)

    ctx = {
        'error': None,
        'name': patient.name,
        'phone': patient.phone,
        'date_of_birth': patient.date_of_birth.strftime('%Y-%m-%d'),
        'submit_button_text': 'Update Patient'
    }

    # Handle form submission
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        date_of_birth = request.POST.get('date_of_birth')
        ctx.update({'name': name, 'phone': phone, 'date_of_birth': date_of_birth})

        if not name or not phone or not date_of_birth:
            ctx.update({'error': "All fields are required."})
        else:
            patient.name = name
            patient.phone = phone
            patient.date_of_birth = date_of_birth
            patient.save()
            return redirect('patient_details', patient_id=patient.id)

    return render(request, 'patient_form.html', ctx)

def delete_patient(request, patient_id):
    patient = get_object_or_404(Patient, id=patient_id)

    if request.method == 'POST':
        patient.delete()
        return redirect('patient_list')

    return render(request, 'delete_patient.html', {'patient': patient})