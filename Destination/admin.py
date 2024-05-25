from django.contrib import admin
from .models import Destination, DestinationDetails, TransportationOption, DestinationAdditionalInfo, DestinationImage

class DestinationDetailsInline(admin.StackedInline):
    model = DestinationDetails
    extra = 1

class TransportationOptionInline(admin.TabularInline):
    model = TransportationOption
    extra = 1

class DestinationAdditionalInfoInline(admin.StackedInline):
    model = DestinationAdditionalInfo
    extra = 1

class DestinationImageInline(admin.TabularInline):
    model = DestinationImage
    extra = 1

@admin.register(Destination)
class DestinationAdmin(admin.ModelAdmin):
    inlines = [DestinationDetailsInline, TransportationOptionInline, DestinationAdditionalInfoInline, DestinationImageInline]

    list_display = ('name', 'location', 'average_rating')
    search_fields = ('name', 'location')

    fieldsets = (
        ('Basic Information', {
            'fields': ('name', 'description','price', 'location', 'address','Latitude','Longitude', 'contact_phone', 'contact_email', 'website', 'cover_image', 'average_rating')
        }),
    )

@admin.register(DestinationDetails)
class DestinationDetailsAdmin(admin.ModelAdmin):
    list_display = ('destination', 'operating_hours', 'entry_fees')
    search_fields = ('destination__name',)

@admin.register(TransportationOption)
class TransportationOptionAdmin(admin.ModelAdmin):
    list_display = ('destination', 'option')
    search_fields = ('destination__name', 'option')

@admin.register(DestinationAdditionalInfo)
class DestinationAdditionalInfoAdmin(admin.ModelAdmin):
    list_display = ('destination', 'weather_information', 'historical_and_cultural_significance')
    search_fields = ('destination__name',)

