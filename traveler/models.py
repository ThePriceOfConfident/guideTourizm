from django.db import models
from django.contrib.auth.models import User

class Traveler(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField("First Name",max_length=100)
    last_name = models.CharField("Last Name",max_length=100,default="Traveler last name", blank=True)
    email = models.EmailField("Email Adress", blank=True)
    country = models.CharField("Country",max_length=50, default='Turkey')
    city = models.CharField("City",max_length=100, blank=True)
    postal_code = models.CharField("Postal Code",max_length=20, blank=True)
    phone_number = models.CharField("Phone Number",max_length=15, blank=True)
    address = models.CharField("Address",max_length=500, blank=True)
    birth_day = models.DateField('Birthday', blank=True, null=True)
    additional_info = models.TextField("Message",blank=True)

    def __str__(self):
        return f"{self.first_name} - {self.email}"

    class Meta:
        verbose_name_plural = "Travelers"

