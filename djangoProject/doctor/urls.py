from django.urls import path
from django.conf import settings 
from doctor.views import DoctorSearch,FindOpenDoctors,DoctorCreate

urlpatterns = [
    path('search/', DoctorSearch.as_view(), name='doctor-search'),
    path('open/',FindOpenDoctors.as_view(), name='find-open-doctor'),
    path('create/', DoctorCreate.as_view(), name='doctor-create'),
]