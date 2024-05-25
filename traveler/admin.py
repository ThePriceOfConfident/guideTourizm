
from django.contrib import admin
from .models import Traveler

@admin.register(Traveler)
class TravelerAdmin(admin.ModelAdmin):
    list_display = ['first_name','last_name' ,'phone_number', 'email','address']
    search_fields = ['first_name', 'last_name','phone_number']