from django.shortcuts import get_object_or_404, redirect, render

from .models import Appointment
from patients.models import Patient

def appointment_list(request):
    q = request.GET.get('q')
    from_date = request.GET.get('from_date')
    to_date = request.GET.get('to_date')

    if q:
        appointments = Appointment.objects.filter(patient__name__icontains=q)
    else:
        appointments = Appointment.objects.all()

    if from_date:
        appointments = appointments.filter(date__gte=from_date)

    if to_date:
        appointments = appointments.filter(date__lte=to_date)

    return render(request, 'appointment_list.html', {'appointments': appointments})

def new_appointment(request):
    patients = Patient.objects.all()

    if request.method == 'POST':
        patient_id = request.POST.get('patient')
        date = request.POST.get('date')
        time = request.POST.get('time')
        reason = request.POST.get('reason')
        notes = request.POST.get('notes')

        patient = Patient.objects.get(id=patient_id)
        Appointment.objects.create(patient=patient, date=date, time=time, reason=reason, notes=notes)

        return redirect('appointment_list')

    ctx = {
        'patients': patients,
        'button_text': 'Create Appointment',
    }
    
    return render(request, 'appointment_form.html', ctx)

def appointment_details(request, appointment_id):
    appointment = get_object_or_404(Appointment, id=appointment_id)
    return render(request, 'appointment_details.html', {'appointment': appointment})

def edit_appointment(request, appointment_id):
    appointment = get_object_or_404(Appointment, id=appointment_id)
    patients = Patient.objects.all()

    if request.method == 'POST':
        patient_id = request.POST.get('patient')
        date = request.POST.get('date')
        time = request.POST.get('time')
        reason = request.POST.get('reason')
        notes = request.POST.get('notes')

        patient = Patient.objects.get(id=patient_id)
        appointment.patient = patient
        appointment.date = date
        appointment.time = time
        appointment.reason = reason
        appointment.notes = notes
        appointment.save()

        return redirect('appointment_details', appointment_id=appointment.id)

    ctx = {
        'appointment': appointment,
        'patients': patients,
        'button_text': 'Update Appointment',
    }
    return render(request, 'appointment_form.html', ctx )

def delete_appointment(request, appointment_id):
    appointment = get_object_or_404(Appointment, id=appointment_id)

    if request.method == 'POST':
        appointment.delete()
        return redirect('appointment_list')

    return render(request, 'delete_appointment.html', {'appointment': appointment})