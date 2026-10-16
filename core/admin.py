from django.contrib import admin
from .models import Appointment, Booking, Doctor


# ✅ Appointment Admin (Enhanced)
@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = (
        'patient_name',
        'doctor_name',
        'phone',
        'appointment_date',
        'appointment_time',
        'token_number',
        'status'
    )

    list_filter = ('appointment_date', 'doctor_name', 'status')  # 🔍 filter
    search_fields = ('patient_name', 'phone', 'doctor_name')     # 🔎 search
    ordering = ('-appointment_date', '-appointment_time')        # ⬇ latest first


# ✅ Booking Admin (Enhanced)
@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = (
        'patient_name',
        'doctor_name',
        'phone',
        'appointment_date',
        'appointment_time'
    )

    list_filter = ('appointment_date', 'doctor_name')
    search_fields = ('patient_name', 'phone')


# ✅ NEW: Doctor Admin (Dynamic Doctors)
@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    list_display = ('name', 'speciality', 'experience')
    list_filter = ('speciality',)
    search_fields = ('name', 'speciality')