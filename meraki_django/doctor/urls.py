from django.urls import path
from django.conf import settings 
from doctor.views import DoctorSearch,FindOpenDoctors

urlpatterns = [
    path('doctors/search/', DoctorSearch.as_view(), name='doctor-search'),
    path('doctors/open/',FindOpenDoctors.as_view(), name='FindOpenDoctors'),
]