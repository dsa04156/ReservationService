from .models import Doctor
from .serializers import DoctorSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET'])
def DoctorList(request):
    print("================================================")
    # doctors = Doctor.objects.values('doctor_name', 'hospital_name','monday')
    doctors2 = Doctor.objects.all()
    # print("의사 목록",doctors)
    print("의사목록 2 ",doctors2)
    
    serializer = DoctorSerializer(doctors2, many=True)
    print("직렬화된 데이터",serializer.data)
    return Response(serializer.data)