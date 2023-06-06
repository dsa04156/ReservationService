from rest_framework import serializers
from .models import Doctor

class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = '__all__'
        # fields = ('doctor_name','hospital_name')

class DoctorSearchSerializer(serializers.Serializer):
    doctor_name = serializers.CharField()
    hospital_name = serializers.CharField()
    non_reimbursements = serializers.ListField(child=serializers.CharField(), allow_empty=True)
    departments = serializers.ListField(child=serializers.CharField(), allow_empty=True)