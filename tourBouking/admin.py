from django.contrib import admin
from .models import TourBooking

class TourBookingAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'date_time', 'destination', 'number_of_persons', 'number_of_kids')
    list_filter = ('destination', 'date_time', 'special_accommodation')
    search_fields = ['name', 'email', 'phone', 'special_request']

admin.site.register(TourBooking, TourBookingAdmin)

# Customize verbose name for the TourBooking model
TourBooking._meta.verbose_name = "Booking"
TourBooking._meta.verbose_name_plural = "Bookings"