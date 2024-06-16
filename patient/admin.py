from django.contrib import admin
from patient.models import Patient, Treatment


@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display = ["id", "first_name", "last_name", "gender"]


@admin.register(Treatment)
class TreatmentAdmin(admin.ModelAdmin):
    list_display = ["id", "patient", "doctor_name", "disease"]
