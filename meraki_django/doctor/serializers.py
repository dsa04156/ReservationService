from rest_framework import serializers
from .models import Doctor

class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = '__all__'
        # fields = ('doctor_name','hospital_name')

class DoctorSearchSerializer(serializers.Serializer):
    query = serializers.CharField(help_text="검색 내용 입력",required=True)

class OpenSearchSerializer(serializers.Serializer):
    datetime = serializers.CharField(help_text="시간 입력 2022-08-15 08:00:00",required=True)

class DoctorCreateSerializer(serializers.Serializer):
    doctor_name = serializers.CharField(help_text="의사 이름",required=True)
    hospital_name = serializers.CharField(help_text="병원 이름",required=True)
    department_name = serializers.CharField(help_text="진료과 이름",required=True)
    non_reimbursement_name = serializers.CharField(help_text="비급여 과목 이름",required=False, allow_blank=True)
    monday = serializers.CharField(help_text="시간 입력 08:00:00 17:00:00 12:00:00 13:00:00" ,required=False, allow_blank=True)
    tuesday = serializers.CharField(help_text="시간 입력 08:00:00 17:00:00 12:00:00 13:00:00" ,required=False, allow_blank=True)
    wednesday = serializers.CharField(help_text="시간 입력 08:00:00 17:00:00 12:00:00 13:00:00", required=False, allow_blank=True)
    thursday = serializers.CharField(help_text="시간 입력 08:00:00 17:00:00 12:00:00 13:00:00",required=False, allow_blank=True)
    friday = serializers.CharField(help_text="시간 입력 08:00:00 17:00:00 12:00:00 13:00:00",required=False, allow_blank=True)
    saturday = serializers.CharField(help_text="시간 입력 08:00:00 17:00:00 12:00:00 13:00:00",required=False, allow_blank=True)
    sunday = serializers.CharField(help_text="시간 입력 08:00:00 17:00:00 12:00:00 13:00:00",required=False, allow_blank=True)