from django.shortcuts import render
from django.utils import timezone

from patients.models import Patient
from appointments.models import Appointment

def dashboard(request):
     total_patients = Patient.objects.count()
     total_appointments = Appointment.objects.count()
     upcoming_appointments = Appointment.objects.filter(date__gte=timezone.now()).count()
     return render(request, 'dashboard.html', {
         'total_patients': total_patients,
         'total_appointments': total_appointments,
         'upcoming_appointments': upcoming_appointments
     })