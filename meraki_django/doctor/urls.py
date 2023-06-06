from django.urls import path
from . import views

urlpatterns = [
    path('doctors/search/', views.DoctorSearch),
    path('doctors/open/',views.find_open_doctors)
    
]