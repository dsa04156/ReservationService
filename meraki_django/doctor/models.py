from django.db import models


class Patient(models.Model):
    patient_id = models.AutoField(primary_key=True)
    patient_name = models.CharField(max_length=15)

    class Meta:
        db_table = 'patient'


class Departments(models.Model):
    departments_id = models.AutoField(primary_key=True)
    departments_name = models.CharField(max_length=30)

    class Meta:
        db_table = 'departments'


class BusinessHours(models.Model):
    business_hours_id = models.AutoField(primary_key=True)
    start_time = models.TimeField(null=True, blank=True)
    end_time = models.TimeField(null=True, blank=True)
    lunch_start_time = models.TimeField(null=True, blank=True)
    lunch_end_time = models.TimeField(null=True, blank=True)

    class Meta:
        db_table = 'business_hours'


class Doctor(models.Model):
    doctor_id = models.AutoField(primary_key=True)
    doctor_name = models.CharField(max_length=30)
    hospital_name = models.CharField(max_length=30)
    monday = models.ForeignKey(BusinessHours, on_delete=models.CASCADE, null=True, blank=True, related_name='+', db_column='monday')
    tuesday = models.ForeignKey(BusinessHours, on_delete=models.CASCADE, null=True, blank=True, related_name='+', db_column='tuesday')
    wednesday = models.ForeignKey(BusinessHours, on_delete=models.CASCADE, null=True, blank=True, related_name='+', db_column='wednesday')
    thursday = models.ForeignKey(BusinessHours, on_delete=models.CASCADE, null=True, blank=True, related_name='+', db_column='thursday')
    friday = models.ForeignKey(BusinessHours, on_delete=models.CASCADE, null=True, blank=True, related_name='+', db_column='friday')
    saturday = models.ForeignKey(BusinessHours, on_delete=models.CASCADE, null=True, blank=True, related_name='+', db_column='saturday')
    sunday = models.ForeignKey(BusinessHours, on_delete=models.CASCADE, null=True, blank=True, related_name='+', db_column='sunday')

    class Meta:
        db_table = 'doctor'


class DoctorDepartments(models.Model):
    doctor_departments_id = models.AutoField(primary_key=True)
    doctor_id = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    department_id = models.ForeignKey(Departments, on_delete=models.CASCADE)

    class Meta:
        db_table = 'doctor_departments'


class NonReimbursement(models.Model):
    non_reimbursement_id = models.AutoField(primary_key=True)
    non_reimbursement_name = models.CharField(max_length=30)

    class Meta:
        db_table = 'non_reimbursement'


class DoctorNonReimbursement(models.Model):
    doctor_non_reimbursement_id = models.AutoField(primary_key=True)
    doctor_id = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    non_reimbursement_id = models.ForeignKey(NonReimbursement, on_delete=models.CASCADE)

    class Meta:
        db_table = 'doctor_non_reimbursement'


class MedicalAppointment(models.Model):
    medical_appointment_id = models.AutoField(primary_key=True)
    appointment_datetime = models.DateTimeField()
    expiration_datetime = models.DateTimeField()
    status = models.IntegerField(default=0)
    patient_id = models.ForeignKey(Patient, on_delete=models.CASCADE)
    doctor_id = models.ForeignKey(Doctor, on_delete=models.CASCADE)

    class Meta:
        db_table = 'medical_appointment'