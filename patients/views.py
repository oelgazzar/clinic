from django.shortcuts import redirect, render

from .models import Patient

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
        ctx.update({'name': name, 'phone': phone, 'date_of_birth': date_of_birth})

        if not name or not phone or not date_of_birth:
            ctx.update({'error': "All fields are required."})
        else:
            Patient.objects.create(name=name, phone=phone, date_of_birth=date_of_birth)
            return redirect('patient_list')

    return render(request, 'patient_form.html', ctx)

def patient_details(request, patient_id):
    try:
        patient = Patient.objects.get(id=patient_id)
    except Patient.DoesNotExist:
        return render(request, '404.html', status=404)
    return render(request, 'patient_details.html', {'patient': patient})


def edit_patient(request, patient_id):
    try:
        patient = Patient.objects.get(id=patient_id)
    except Patient.DoesNotExist:
        return render(request, '404.html', status=404)

    ctx = {
        'error': None,
        'name': patient.name,
        'phone': patient.phone,
        'date_of_birth': patient.date_of_birth,
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
    try:
        patient = Patient.objects.get(id=patient_id)
    except Patient.DoesNotExist:
        return render(request, '404.html', status=404)

    if request.method == 'POST':
        patient.delete()
        return redirect('patient_list')

    return render(request, 'delete_patient.html', {'patient': patient})