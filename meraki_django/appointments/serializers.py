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


