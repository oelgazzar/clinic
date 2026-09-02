from django import forms

from .models import Appointment

class AppointmentForm(forms.ModelForm):
     class Meta:
         model = Appointment
         fields = '__all__'
         widgets = {
            'patient': forms.Select(attrs={'class': 'form-select mb-3'}),
            'date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control mb-3'}),
            'time': forms.TimeInput(attrs={'type': 'time', 'class': 'form-control mb-3'}),
            'reason': forms.TextInput(attrs={'class': 'form-control mb-3'}),
            'notes': forms.Textarea(attrs={'class': 'form-control mb-3', 'rows': 3}),
            'status': forms.Select(attrs={'class': 'form-select mb-3'}),
         }