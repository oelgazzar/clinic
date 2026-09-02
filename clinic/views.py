from django.shortcuts import render
from django.utils import timezone
from django.contrib.auth.decorators import login_required

from patients.models import Patient
from appointments.models import Appointment

@login_required
def dashboard(request):
     total_patients = Patient.objects.count()
     total_appointments = Appointment.objects.count()
     upcoming_appointments = Appointment.objects.filter(date__gte=timezone.now())
     return render(request, 'dashboard.html', {
         'total_patients': total_patients,
         'total_appointments': total_appointments,
         'upcoming_appointments': upcoming_appointments
     })