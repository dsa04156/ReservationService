from django.db import models


class Patient(models.Model):
    patient_id = models.AutoField(primary_key=True)
    patient_name = models.CharField(max_length=15)

    class Meta:
        db_table = 'patient'


class Department(models.Model):
    department_id = models.AutoField(primary_key=True)
    department_name = models.CharField(max_length=30)

    class Meta:
        db_table = 'department'


class BusinessHour(models.Model):
    business_hour_id = models.AutoField(primary_key=True)
    start_time = models.TimeField(null=True, blank=True)
    end_time = models.TimeField(null=True, blank=True)
    lunch_start_time = models.TimeField(null=True, blank=True)
    lunch_end_time = models.TimeField(null=True, blank=True)

    class Meta:
        db_table = 'business_hour'


class Doctor(models.Model):
    doctor_id = models.AutoField(primary_key=True)
    doctor_name = models.CharField(max_length=30)
    hospital_name = models.CharField(max_length=30)
    monday = models.ForeignKey(BusinessHour, on_delete=models.CASCADE, null=True, blank=True, related_name='+', db_column='monday')
    tuesday = models.ForeignKey(BusinessHour, on_delete=models.CASCADE, null=True, blank=True, related_name='+', db_column='tuesday')
    wednesday = models.ForeignKey(BusinessHour, on_delete=models.CASCADE, null=True, blank=True, related_name='+', db_column='wednesday')
    thursday = models.ForeignKey(BusinessHour, on_delete=models.CASCADE, null=True, blank=True, related_name='+', db_column='thursday')
    friday = models.ForeignKey(BusinessHour, on_delete=models.CASCADE, null=True, blank=True, related_name='+', db_column='friday')
    saturday = models.ForeignKey(BusinessHour, on_delete=models.CASCADE, null=True, blank=True, related_name='+', db_column='saturday')
    sunday = models.ForeignKey(BusinessHour, on_delete=models.CASCADE, null=True, blank=True, related_name='+', db_column='sunday')

    class Meta:
        db_table = 'doctor'


class DoctorDepartment(models.Model):
    doctor_department_id = models.AutoField(primary_key=True)
    doctor_id = models.ForeignKey(Doctor, on_delete=models.CASCADE, related_name='doctor_department',db_column='doctor_id')
    department_id = models.ForeignKey(Department, related_name='doctor_department',on_delete=models.CASCADE,db_column='department_id')

    class Meta:
        db_table = 'doctor_department'


class NonReimbursement(models.Model):
    non_reimbursement_id = models.AutoField(primary_key=True)
    non_reimbursement_name = models.CharField(max_length=30)

    class Meta:
        db_table = 'non_reimbursement'


class DoctorNonReimbursement(models.Model):
    doctor_non_reimbursement_id = models.AutoField(primary_key=True)
    doctor_id = models.ForeignKey(Doctor, on_delete=models.CASCADE,related_name='doctor_non_reimbursement',db_column='doctor_id')
    non_reimbursement_id = models.ForeignKey(NonReimbursement, on_delete=models.CASCADE,related_name='doctor_non_reimbursement',db_column='non_reimbursement_id')

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