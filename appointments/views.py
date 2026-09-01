from django.shortcuts import get_object_or_404, redirect, render

from .models import Appointment
from patients.models import Patient
from .forms import AppointmentForm

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
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('appointment_list')
    else:
        form = AppointmentForm()
    return render(request, 'appointment_form.html', {'form': form, 'button_text': 'Create Appointment'})

def appointment_details(request, appointment_id):
    appointment = get_object_or_404(Appointment, id=appointment_id)
    return render(request, 'appointment_details.html', {'appointment': appointment})

def edit_appointment(request, appointment_id):
    appointment = get_object_or_404(Appointment, id=appointment_id)

    if request.method == 'POST':
        form = AppointmentForm(request.POST, instance=appointment)
        if form.is_valid():
            form.save()
            return redirect('appointment_details', appointment_id=appointment.id)
    else:
        form = AppointmentForm(instance=appointment)
    return render(request, 'appointment_form.html', {'form': form, 'button_text': 'Update Appointment'})

def delete_appointment(request, appointment_id):
    appointment = get_object_or_404(Appointment, id=appointment_id)

    if request.method == 'POST':
        appointment.delete()
        return redirect('appointment_list')

    return render(request, 'delete_appointment.html', {'appointment': appointment})