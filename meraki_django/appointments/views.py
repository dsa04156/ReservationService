from django.shortcuts import render
from .serializers import AppointmentRequestCreateSerializer,AppointmentRequestResponseSerializer
from doctor.models import Doctor,BusinessHour
from .models import MedicalAppointment,Patient
# Create your views here.
from drf_yasg.utils import swagger_auto_schema
from rest_framework.response import Response
from rest_framework.views import APIView
from drf_yasg import openapi
from django.db.models import Q
from rest_framework import status
from datetime import datetime,timedelta
from django.utils import timezone

class AppointmentRequest(APIView):
    @swagger_auto_schema(
        tags=['진료를 요청합니다.'],
        query_serializer=AppointmentRequestCreateSerializer,
        responses={200: openapi.Response('Success')}
    )
    def post(self, request):
        patient_id = request.GET.get('patient_id')
        doctor_id = request.GET.get('doctor_id')
        appointment_datetime = request.GET.get('appointment_datetime')
        appointment_datetime = datetime.strptime(appointment_datetime, '%Y-%m-%d %H:%M:%S')
        # 환자 정보 가져오기
        try:
            patient = Patient.objects.get(patient_id=patient_id)
        except Patient.DoesNotExist:
            return Response({'error': '환자를 찾을 수 없습니다.'}, status=status.HTTP_400_BAD_REQUEST)
        # 의사 정보 가져오기
        try:
            doctor = Doctor.objects.get(doctor_id=doctor_id)
        except Doctor.DoesNotExist:
            return Response({'error': '의사를 찾을 수 없습니다.'}, status=status.HTTP_400_BAD_REQUEST)

        # 예약 만료 시간 계산
    
        expiration_datetime = self.calculate_expiration_datetime(appointment_datetime, doctor)
        print(appointment_datetime)
        print(expiration_datetime)
        
        # 예약 생성
        appointment = MedicalAppointment.objects.create(
            appointment_datetime=appointment_datetime,
            expiration_datetime=expiration_datetime,
            status=0,
            patient_id=patient,
            doctor_id=doctor
        )
        # appointment.save()
        # 예약 정보 응답
        serializer = AppointmentRequestResponseSerializer(appointment)
        return Response("성공", status=status.HTTP_200_OK)

    def calculate_expiration_datetime(self, appointment_datetime, doctor):
        # 요일별 영업 시간 가져오기
        weekday_field = appointment_datetime.strftime('%A').lower()
        business_hour = getattr(doctor, weekday_field, None)
        if business_hour is None:
            # 해당 요일의 영업 시간이 없는 경우, 예약 만료 시간을 다음 영업 시작 시간 + 15분으로 설정
            next_business_hour = self.get_next_business_hour(appointment_datetime, doctor)
            if next_business_hour is None:
                return None  # 다음 영업일의 영업 시간이 없는 경우, 예약 만료 시간을 설정할 수 없음
            expiration_datetime = datetime.combine(appointment_datetime.date(), next_business_hour) + timedelta(minutes=15)
        else:
            # 해당 요일의 영업 시간이 있는 경우
            if business_hour.start_time <= appointment_datetime.time() < business_hour.end_time:
                # 예약 시간이 영업 시간 내에 있는 경우
                if business_hour.lunch_start_time and business_hour.lunch_end_time:
                    # 점심 시간인 경우, 예약 만료 시간을 점심 종료 시간 + 15분으로 설정
                    if business_hour.lunch_start_time <= appointment_datetime.time() < business_hour.lunch_end_time:
                        expiration_datetime = datetime.combine(appointment_datetime.date(), business_hour.lunch_end_time) + timedelta(minutes=15)
                    else:
                        expiration_datetime = appointment_datetime + timedelta(minutes=20)
                else:
                    # 점심 시간이 없는 경우, 예약 만료 시간을 영업 종료 시간 + 15분으로 설정
                    expiration_datetime = datetime.combine(appointment_datetime.date(), business_hour.end_time) + timedelta(minutes=15)
            else:
                # 예약 시간이 영업 시간 밖에 있는 경우, 예약 만료 시간을 다음 영업 시작 시간 + 15분으로 설정
                next_business_hour = self.get_next_business_hour(appointment_datetime, doctor)
                if next_business_hour is None:
                    return None  # 다음 영업일의 영업 시간이 없는 경우, 예약 만료 시간을 설정할 수 없음
                expiration_datetime = datetime.combine(appointment_datetime.date(), next_business_hour) + timedelta(minutes=15)
        print("최종 시간",expiration_datetime)
        return expiration_datetime


    def get_next_business_hour(self, appointment_datetime, doctor):
        current_weekday = appointment_datetime.weekday()
        next_weekday = current_weekday
        print("aaaa")
        next_weekday = appointment_datetime
        cnt=0
        while True:
            next_weekday = next_weekday + timedelta(days=1)

            next_weekday_field = next_weekday.strftime('%A').lower()
            print(next_weekday_field)
            next_business_hour = getattr(doctor, next_weekday_field, None)
            if next_business_hour is not None:
                print("완료", next_business_hour.start_time)
                return next_business_hour.start_time
            cnt+=1
            if cnt==7:
                break  # 현재 요일로 돌아온 경우, 모든 요일을 확인했으므로 종료
        return None
    
class SearchMedicalAppointments(APIView):
    doctor_id = openapi.Parameter('doctor_id', openapi.IN_QUERY, description='doctor_id param', required=True,  type=openapi.TYPE_INTEGER)
    @swagger_auto_schema(
        tags=['진료 요청 목록을 검색합니다'],
        manual_parameters=[doctor_id],
        responses={200: openapi.Response('Success')}
    )
    def get(self, request):
        doctor_id = int(request.GET.get('doctor_id'))

            # 진료요청 검색 쿼리
        medical_appointments = MedicalAppointment.objects.filter(
            doctor_id=doctor_id
        ).exclude(status=1)
            # 결과 반환

        result = []
        for appointment in medical_appointments:
            result.append({
                'medical_appointment_id': appointment.medical_appointment_id,
                'patient_name': appointment.patient_id.patient_name,
                'appointment_datetime': appointment.appointment_datetime,
                'expiration_datetime': appointment.expiration_datetime
            })

        return Response(result, status=status.HTTP_200_OK)
    
class AcceptMedicalAppointment(APIView):
    medical_appointment_id = openapi.Parameter('medical_appointment_id', openapi.IN_QUERY, description='medical_appointment_id param', required=True,  type=openapi.TYPE_INTEGER)
    @swagger_auto_schema(
        tags=['진료 요청을 수락합니다.'],
        manual_parameters=[medical_appointment_id],
        responses={200: openapi.Response('Success')}
    )
    def get(self,request):
        medical_appointment_id = request.GET.get('medical_appointment_id')
        print(medical_appointment_id)
            
        try:
            appointment = MedicalAppointment.objects.get(medical_appointment_id=medical_appointment_id)
            
            # 이미 수락된 진료요청인 경우 예외 처리
            if appointment.status == 1:
                return Response("이미 수락된 진료요청입니다.", status=status.HTTP_400_BAD_REQUEST)
            
            # 수락 상태로 변경
            appointment.status = 1
            appointment.save()
            
            # 결과 반환
            result = {
                'medical_appointment_id': appointment.medical_appointment_id,
                'patient_name': appointment.patient_id.patient_name,
                'appointment_datetime': appointment.appointment_datetime,
                'expiration_datetime': appointment.expiration_datetime
            }
            
            return Response(result, status=status.HTTP_200_OK)
        
        except MedicalAppointment.DoesNotExist:
            return Response("해당 진료요청을 찾을 수 없습니다.", status=status.HTTP_404_NOT_FOUND)