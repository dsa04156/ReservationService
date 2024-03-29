from .models import Doctor,BusinessHour,Department,NonReimbursement, DoctorDepartment, DoctorNonReimbursement
from .serializers import DoctorSearchSerializer,OpenSearchSerializer,DoctorCreateSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from django.db import connection
from django.db.models import Q
from datetime import datetime
from drf_yasg.utils import swagger_auto_schema
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi       
from django.db import transaction 


# http://127.0.0.1:8000/api/doctors/search/?query={검색값}
# @api_view(['GET'])
class DoctorSearch(APIView):
    @swagger_auto_schema(
        tags=['데이터를 검색합니다.'],
        query_serializer=DoctorSearchSerializer,
        responses={200: openapi.Response('Success')}
    )
    def get(self,request):
        query = request.GET.get('query',None)
        search_terms = query.split()   
        conditions = Q()
        for term in search_terms:
            conditions &= (Q(doctor_name__icontains=term) |
                        Q(hospital_name__icontains=term) |
                        Q(doctor_department__department_id__department_name__icontains=term) |
                        Q(doctor_non_reimbursement__non_reimbursement_id__non_reimbursement_name__icontains=term))

        doctors = Doctor.objects.filter(conditions).distinct()

        formatted_names = []

        for doctor in doctors:
            formatted_name = f"{doctor.doctor_name}의사"
            formatted_names.append(formatted_name)
        return Response(formatted_names,status=200)

class FindOpenDoctors(APIView):
    @swagger_auto_schema(
        tags=['데이터를 검색합니다.'],
        query_serializer=OpenSearchSerializer,
        responses={200: openapi.Response('Success')}
    )
    def get(self, request):
        query = request.GET.get('datetime')  # 입력된 날짜와 시간을 가져옵니다.
        format_string = '%Y-%m-%d %H:%M:%S'  # 입력된 날짜와 시간의 형식을 지정합니다.

        try:
            # 입력된 날짜와 시간을 datetime 객체로 변환합니다.
            datetime_obj = datetime.strptime(query, format_string)

            # 입력된 날짜와 시간의 요일을 가져옵니다. (0: 월요일, 6: 일요일)
            weekday = datetime_obj.weekday()

            # 요일에 해당하는 필드 이름을 설정합니다.
            weekday_fields = [
                'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday'
            ]
            fieldname = weekday_fields[weekday]

            # 입력된 시간이 영업 시간에 포함되는 의사를 조회합니다.
            doctors = Doctor.objects.filter(
                Q(**{f'{fieldname}__start_time__lte': datetime_obj.time()}) &
                Q(**{f'{fieldname}__end_time__gt': datetime_obj.time()})
            )

            # 영업중인 의사의 이름을 반환합니다.
            formatted_names = [f"{doctor.doctor_name}의사" for doctor in doctors]

            return Response(formatted_names, status=status.HTTP_200_OK)
        except ValueError:
            return Response("Invalid datetime format", status=status.HTTP_400_BAD_REQUEST)
        
class DoctorCreate(APIView):
    @swagger_auto_schema(
        tags=['의사 데이터를 생성합니다.'],
        request_body=DoctorCreateSerializer,
        responses={200: openapi.Response('Success')}
    )
    @transaction.atomic
    def post(self,request):
        data = request.data
        doctor_name = data.get('doctor_name')
        hospital_name = data.get('hospital_name')
        department_name = data.get('department_name')
        non_reimbursed_name = data.get('non_reimbursement_name')
        monday = data.get('monday')
        tuesday = data.get('tuesday')
        wednesday = data.get('wednesday')
        thursday = data.get('thursday')
        friday = data.get('friday')
        saturday = data.get('saturday')
        sunday = data.get('sunday')
        doctor = Doctor.objects.create(doctor_name=doctor_name, hospital_name=hospital_name)

                # 월요일 영업시간 데이터 처리
        if monday:
            start_time, end_time, lunch_start_time, lunch_end_time = monday.split(' ')
            business_hour = BusinessHour.objects.create(
                start_time=start_time,
                end_time=end_time,
                lunch_start_time=lunch_start_time,
                lunch_end_time=lunch_end_time
            )
            doctor.monday = business_hour
        
        # 화요일 영업시간 데이터 처리
        if tuesday:
            start_time, end_time, lunch_start_time, lunch_end_time = tuesday.split(' ')
            business_hour = BusinessHour.objects.create(
                start_time=start_time,
                end_time=end_time,
                lunch_start_time=lunch_start_time,
                lunch_end_time=lunch_end_time
            )
            doctor.tuesday = business_hour
        
        # 수요일 영업시간 데이터 처리
        if wednesday:
            start_time, end_time, lunch_start_time, lunch_end_time = wednesday.split(' ')
            business_hour = BusinessHour.objects.create(
                start_time=start_time,
                end_time=end_time,
                lunch_start_time=lunch_start_time,
                lunch_end_time=lunch_end_time
            )
            doctor.wednesday = business_hour
        
        # 목요일 영업시간 데이터 처리
        if thursday:
            start_time, end_time, lunch_start_time, lunch_end_time = thursday.split(' ')
            business_hour = BusinessHour.objects.create(
                start_time=start_time,
                end_time=end_time,
                lunch_start_time=lunch_start_time,
                lunch_end_time=lunch_end_time
            )
            doctor.thursday = business_hour
        
        # 금요일 영업시간 데이터 처리
        if friday:
            start_time, end_time, lunch_start_time, lunch_end_time = friday.split(' ')
            business_hour = BusinessHour.objects.create(
                start_time=start_time,
                end_time=end_time,
                lunch_start_time=lunch_start_time,
                lunch_end_time=lunch_end_time
            )
            doctor.friday = business_hour
        
        if saturday:
            start_time, end_time, lunch_start_time, lunch_end_time = saturday.split(' ')
            business_hour = BusinessHour.objects.create(
                start_time=start_time,
                end_time=end_time,
                lunch_start_time=lunch_start_time,
                lunch_end_time=lunch_end_time
            )
            doctor.saturday = business_hour

        if sunday:
            start_time, end_time, lunch_start_time, lunch_end_time = sunday.split(' ')
            business_hour = BusinessHour.objects.create(
                start_time=start_time,
                end_time=end_time,
                lunch_start_time=lunch_start_time,
                lunch_end_time=lunch_end_time
            )
            doctor.sunday = business_hour
        
        doctor.save()
        
        # 진료과 데이터 삽입
        department, _ = Department.objects.get_or_create(department_name=department_name)
        DoctorDepartment.objects.create(doctor_id=doctor, department_id=department)
        
        print(non_reimbursed_name)
        # 비급여 과목 데이터 삽입
        if non_reimbursed_name:
            non_reimbursement, _ = NonReimbursement.objects.get_or_create(non_reimbursement_name=non_reimbursed_name)
            DoctorNonReimbursement.objects.create(doctor_id=doctor, non_reimbursement_id=non_reimbursement)
            print("생성했따")

        return Response("성공", status=status.HTTP_200_OK)
        
    
