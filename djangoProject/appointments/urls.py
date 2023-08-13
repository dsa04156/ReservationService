from django.urls import path
from django.conf import settings 
from appointments.views import AppointmentRequest,SearchMedicalAppointments,AcceptMedicalAppointment,CreatePatient,GetPatient,GetDoctor

urlpatterns = [
    path('request/', AppointmentRequest.as_view(), name='appointment-request'),
    path('search/', SearchMedicalAppointments.as_view(), name='search-medical-appointments'),
    path('accept/',AcceptMedicalAppointment.as_view(), name='accept-medical-appointments'),
    path('patient/',CreatePatient.as_view(), name='create-patient'),
    path('patient/list/',GetPatient.as_view(), name='get-patient'),
    path('doctor/list/',GetDoctor.as_view(), name='get-doctor'),
]