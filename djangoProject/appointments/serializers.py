from rest_framework import serializers


class AppointmentRequestCreateSerializer(serializers.Serializer):
    patient_id = serializers.IntegerField(help_text="환자 id", required=True)
    doctor_id = serializers.IntegerField(help_text="의사 id", required=True)
    appointment_datetime = serializers.DateTimeField(help_text="예약 시간", required=True)

class AppointmentRequestResponseSerializer(serializers.Serializer):
    medical_appointment_id = serializers.IntegerField(help_text="진료요청 id")
    patient_name = serializers.CharField(help_text="환자 이름")
    doctor_name = serializers.CharField(help_text="의사 이름")
    appointment_time = serializers.DateTimeField(help_text="진료 희망 날짜시간")
    expiration_time = serializers.DateTimeField(help_text="진료요청 만료 날짜시간")

class PatientListSerializer(serializers.Serializer):
    patient_id = serializers.CharField(help_text="환자 id")
    patient_name = serializers.CharField(help_text="환자 이름")

class DoctorListSerializer(serializers.Serializer):
    doctor_id = serializers.IntegerField(help_text="의사 id")
    doctor_name = serializers.CharField(help_text="의사 이름",required=True)
    hospital_name = serializers.CharField(help_text="병원 이름",required=True)
    monday = serializers.CharField(help_text="시간 입력 08:00:00 17:00:00 12:00:00 13:00:00" ,required=False, allow_blank=True)
    tuesday = serializers.CharField(help_text="시간 입력 08:00:00 17:00:00 12:00:00 13:00:00" ,required=False, allow_blank=True)
    wednesday = serializers.CharField(help_text="시간 입력 08:00:00 17:00:00 12:00:00 13:00:00", required=False, allow_blank=True)
    thursday = serializers.CharField(help_text="시간 입력 08:00:00 17:00:00 12:00:00 13:00:00",required=False, allow_blank=True)
    friday = serializers.CharField(help_text="시간 입력 08:00:00 17:00:00 12:00:00 13:00:00",required=False, allow_blank=True)
    saturday = serializers.CharField(help_text="시간 입력 08:00:00 17:00:00 12:00:00 13:00:00",required=False, allow_blank=True)
    sunday = serializers.CharField(help_text="시간 입력 08:00:00 17:00:00 12:00:00 13:00:00",required=False, allow_blank=True)

