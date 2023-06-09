from django.db import models
from doctor.models import Doctor
from doctor.models import BusinessHour
class Patient(models.Model):
    patient_id = models.AutoField(primary_key=True,db_column='patient_id')
    patient_name = models.CharField(max_length=15,db_column='patient_name')

    class Meta:
        db_table = 'patient'

class MedicalAppointment(models.Model):
    medical_appointment_id = models.AutoField(primary_key=True,db_column='medical_appointment_id')
    appointment_datetime = models.DateTimeField(db_column='appointment_datetime')
    expiration_datetime = models.DateTimeField(db_column='expiration_datetime')
    status = models.IntegerField(default=0,db_column='status')
    patient_id = models.ForeignKey(Patient, on_delete=models.CASCADE,db_column='patient_id')
    doctor_id = models.ForeignKey(Doctor, on_delete=models.CASCADE,db_column='doctor_id')

    class Meta:
        db_table = 'medical_appointment'