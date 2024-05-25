from django.db import models
from Destination.models import Destination

class TourBooking(models.Model):
    ACCOMMODATION_CHOICES = [
        ('none', 'No Special Accommodation Required'),
        ('wheelchair', 'Wheelchair Access Required'),
        ('visual', 'Visual Assistance Required'),
        ('hearing', 'Hearing Assistance Required'),
        ('other', 'Other (Please Specify in Special Requests)')
    ]

    name = models.CharField(
        max_length=100,
        verbose_name="Name",
         blank=True,
    )
    email = models.EmailField(
        verbose_name="Email"
    )
    phone = models.CharField(
        max_length=20, 
        blank=True,
        verbose_name="Contact Phone"
    )
    date_time = models.DateTimeField(
        verbose_name="Date and Time",
         blank=True,
    )
    destination = models.ForeignKey(
        Destination, 
        on_delete=models.CASCADE, 
        verbose_name="Destination"
    )
    number_of_persons = models.IntegerField(
        verbose_name="Number of Persons",
         blank=True,
         default=1
    )
    number_of_kids = models.IntegerField(
        verbose_name="Number of Kids",
         blank=True,
         default=0
    )
    special_request = models.TextField(
        blank=True, 
        null=True, 
        verbose_name="Special Requests"
    )
    special_accommodation = models.CharField(
        max_length=100, 
        choices=ACCOMMODATION_CHOICES, 
        default='none', 
        verbose_name="Special Accommodation Needs"
    )

    def __str__(self):
        return f"{self.name} booking for {self.destination.name} on {self.date_time.strftime('%Y-%m-%d %H:%M')}"

    class Meta:
        verbose_name = "Tour Booking"
        verbose_name_plural = "Tour Bookings"
