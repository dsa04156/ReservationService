from django.urls import path
from django.conf import settings 
from appointments.views import AppointmentRequest,SearchMedicalAppointments,AcceptMedicalAppointment

urlpatterns = [
    path('request/', AppointmentRequest.as_view(), name='appointment-request'),
    path('search/', SearchMedicalAppointments.as_view(), name='search-medical-appointments'),
    path('accept/',AcceptMedicalAppointment.as_view(), name='accept-medical-appointments'),
]