from .models import Doctor
from .serializers import DoctorSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.db import connection
from django.db.models import Q
from datetime import datetime

# http://127.0.0.1:8000/api/doctors/search/?query={검색값}
@api_view(['GET'])
def DoctorSearch(request):
    query = request.GET.get('query')  # Get the input string
    search_terms = query.split()  # Split the input into search terms

    # Create the filtering conditions based on the search terms
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
    return Response(formatted_names)

@api_view(['GET'])
def find_open_doctors(request):
    query = request.GET.get('datetime')  # 입력된 날짜와 시간을 가져옵니다.
    query= '2022-01-11 15:00:00'
    format_string = '%Y-%m-%d %H:%M:%S'  # 입력된 날짜와 시간의 형식을 지정합니다.

    # 입력된 날짜와 시간을 datetime 객체로 변환합니다.
    datetime_obj = datetime.strptime(query, format_string)

    # 입력된 날짜와 시간의 요일을 가져옵니다. (0: 월요일, 6: 일요일)
    weekday = datetime_obj.weekday()

    # 입력된 시간이 영업 시간에 포함되는 의사를 조회합니다.
    doctors = Doctor.objects.filter(
        Q(monday__start_time__lte=datetime_obj.time(), monday__end_time__gt=datetime_obj.time()) |
        Q(tuesday__start_time__lte=datetime_obj.time(), tuesday__end_time__gt=datetime_obj.time()) |
        Q(wednesday__start_time__lte=datetime_obj.time(), wednesday__end_time__gt=datetime_obj.time()) |
        Q(thursday__start_time__lte=datetime_obj.time(), thursday__end_time__gt=datetime_obj.time()) |
        Q(friday__start_time__lte=datetime_obj.time(), friday__end_time__gt=datetime_obj.time()) |
        Q(saturday__start_time__lte=datetime_obj.time(), saturday__end_time__gt=datetime_obj.time()) |
        Q(sunday__start_time__lte=datetime_obj.time(), sunday__end_time__gt=datetime_obj.time())
    )

    # 영업중인 의사의 이름을 반환합니다.
    doctor_names = [doctor.doctor_name for doctor in doctors]

    return Response(doctor_names)