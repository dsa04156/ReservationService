from django.db import models

class BusinessHours(models.Model):
    business_hours_id = models.IntegerField(primary_key=True)
    start_time = models.TimeField(null=True, blank=True)
    end_time = models.TimeField(null=True, blank=True)
    lunch_start_time = models.TimeField(null=True, blank=True)
    lunch_end_time = models.TimeField(null=True, blank=True)

    class Meta:
        db_table = 'business_hours'
        
class Doctor(models.Model):
    doctor_id = models.IntegerField(primary_key=True)
    doctor_name = models.CharField(max_length=30, blank=False)
    hospital_name = models.CharField(max_length=30, blank=False)
    monday = models.ForeignKey(BusinessHours, on_delete=models.SET_NULL, null=True, blank=True, related_name='+')
    tuesday = models.ForeignKey(BusinessHours, on_delete=models.SET_NULL, null=True, blank=True, related_name='+')
    wednesday = models.ForeignKey(BusinessHours, on_delete=models.SET_NULL, null=True, blank=True, related_name='+')
    thursday = models.ForeignKey(BusinessHours, on_delete=models.SET_NULL, null=True, blank=True, related_name='+')
    friday = models.ForeignKey(BusinessHours, on_delete=models.SET_NULL, null=True, blank=True, related_name='+')
    saturday = models.ForeignKey(BusinessHours, on_delete=models.SET_NULL, null=True, blank=True, related_name='+')
    sunday = models.ForeignKey(BusinessHours, on_delete=models.SET_NULL, null=True, blank=True, related_name='+')
    class Meta:
        db_table = 'doctor'

