from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


# ==========================
# Appointment Model (Main Booking Table)
# ==========================

class Appointment(models.Model):

    patient_name = models.CharField(max_length=100)

    GENDER_CHOICES = [
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other'),
    ]
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)

    phone = models.CharField(max_length=15)

    # Doctor stored as TEXT from dropdown
    doctor_name = models.CharField(max_length=200)

    appointment_date = models.DateField()
    appointment_time = models.TimeField()

    reason = models.TextField(blank=True)

    # Additional professional medical record fields
    doctor_notes = models.TextField(blank=True)
    prescription = models.TextField(blank=True)

    token_number = models.PositiveIntegerField(default=1)

    STATUS_CHOICES = [
        ('Waiting', 'Waiting'),
        ('Now Serving', 'Now Serving'),
        ('Completed', 'Completed'),
        ('Cancelled', 'Cancelled'),
    ]

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='Waiting'
    )

    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.patient_name} - {self.appointment_date}"


# ==========================
# Booking Model (Optional – if login needed)
# ==========================

class Booking(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)

    patient_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)

    doctor_name = models.CharField(max_length=200)

    appointment_date = models.DateField()
    appointment_time = models.TimeField()

    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.patient_name} - {self.appointment_date}"
class Doctor(models.Model):
    name = models.CharField(max_length=100)
    speciality = models.CharField(max_length=100)
    image = models.ImageField(upload_to='doctors/')
    experience = models.IntegerField()

    def __str__(self):
        return self.name