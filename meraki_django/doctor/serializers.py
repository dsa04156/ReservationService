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
    datetime = serializers.CharField(help_text="시간 입력",required=True)