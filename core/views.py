from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Appointment, Booking, Doctor
import datetime


# ------------------------------
# Static Pages
# ------------------------------
def home(request):
    return render(request, 'core/home.html')

def dashboard(request):
    return render(request, 'core/dashboard.html')

def insurance(request):
    return render(request, 'core/insurance.html')

def services(request):
    return render(request, 'core/services.html')

def specialities(request):
    return render(request, 'core/specialities.html')

def contact(request):
    return render(request, 'core/contact.html')

def about(request):
    return render(request, 'core/about.html')

def admin(request):
    return render(request, 'core/admin.html')

def patient(request):
    return render(request, 'core/patient.html')

def confirm(request):
    return render(request, 'core/confirm.html')


# ------------------------------
# Doctors Page
# ------------------------------
def doctors(request):
    doctors = Doctor.objects.all()

    # Group doctors by speciality
    grouped_doctors = {}
    for doc in doctors:
        if doc.speciality not in grouped_doctors:
            grouped_doctors[doc.speciality] = []
        grouped_doctors[doc.speciality].append(doc)

    return render(request, 'core/doctors.html', {
        'grouped_doctors': grouped_doctors
    })


# ------------------------------
# Queue Management (Optimized)
# ------------------------------
def queue(request):
    appointments = Appointment.objects.all().order_by('token_number')
    now = datetime.datetime.now()

    for appt in appointments:
        appt_time = datetime.datetime.combine(
        appt.appointment_date,
        appt.appointment_time
)

        # Update status (without unnecessary DB writes)
        if now > appt_time and appt.status != "Completed":
            appt.status = "Completed"
            appt.save()
        elif now <= appt_time and appt.status != "Waiting":
            appt.status = "Waiting"
            appt.save()

    current_patient = Appointment.objects.filter(
        status="Waiting"
    ).order_by("token_number").first()

    return render(request, "core/queue.html", {
        "appointments": appointments,
        "current_patient": current_patient
    })


def next_patient(request):
    next_app = Appointment.objects.filter(
        status='Waiting'
    ).order_by('token_number').first()

    if next_app:
        next_app.status = 'Now Serving'
        next_app.save()

    return redirect('queue')


# ------------------------------
# Appointment Booking (Improved)
# ------------------------------
def appointment(request):
    # Get doctor details from URL
    doctor_name = request.GET.get('name')
    doctor_spec = request.GET.get('spec')

    if request.method == "POST":
        patient_name = request.POST['patient_name']
        gender = request.POST['gender']
        phone = request.POST['phone']
        doctor = request.POST['doctor']
        speciality = request.POST['speciality']
        appointment_date = request.POST['appointment_date']
        reason = request.POST.get('reason', '')

        hour = int(request.POST.get('hour'))
        minute = int(request.POST.get('minute'))
        ampm = request.POST.get('ampm')

        if ampm == "PM" and hour != 12:
            hour += 12
        if ampm == "AM" and hour == 12:
            hour = 0

        appointment_time = datetime.time(hour, minute)

        token = Appointment.objects.filter(
            appointment_date=appointment_date
        ).count() + 1

        Appointment.objects.create(
            patient_name=patient_name,
            gender=gender,
            phone=phone,
            doctor_name=doctor,
            appointment_date=appointment_date,
            appointment_time=appointment_time,
            reason=reason,
            token_number=token
        )

        return redirect('confirm')

    return render(request, 'core/appointment.html', {
        'doctor_name': doctor_name,
        'doctor_spec': doctor_spec
    })
# ------------------------------
# Insurance Details
# ------------------------------
def insurance_detail(request, insurance_type):
    details = {
        'star_health': "Full details about Star Health Insurance...",
        'icici_lombard': "Full details about ICICI Lombard...",
        'hdfc_ergo': "Full details about HDFC Ergo...",
        'bajaj_allianz': "Full details about Bajaj Allianz..."
    }

    return render(request, 'core/insurance_detail.html', {
        'insurance_type': insurance_type,
        'info': details.get(insurance_type, "No details available.")
    })
def patient_history(request):
    appointments = Appointment.objects.all().order_by('-appointment_date')

    return render(request, 'core/patient_history.html', {
        'appointments': appointments
    })