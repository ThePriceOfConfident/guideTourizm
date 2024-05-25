from django.urls import path
from .views import add_tour_booking, booking_success

urlpatterns = [
    path('add-booking/', add_tour_booking, name='add_tour_booking'),    
    path('booking-success/<int:booking_id>/', booking_success, name='success_booking'),
]