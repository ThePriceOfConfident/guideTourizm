from django.db import models

class Destination(models.Model):
    created = models.DateTimeField(auto_now_add=True, verbose_name="Created")
    updated = models.DateTimeField(auto_now=True, verbose_name="Updated")
    name = models.CharField(verbose_name="Name", max_length=200)
    description = models.TextField(verbose_name="Description", blank=True)
    location = models.CharField(verbose_name="Location", max_length=500)
    address = models.CharField(verbose_name="Address", max_length=500, blank=True)
    contact_phone = models.CharField(verbose_name="Contact Phone", max_length=20, blank=True)
    contact_email = models.EmailField(verbose_name="Contact Email", blank=True)
    website = models.URLField(verbose_name="Website", blank=True)
    cover_image =  models.ImageField(verbose_name="Cover Image",null=True, blank=True, upload_to="destination_images/covers") 
    galery = models.CharField(verbose_name="Galery",null=True, blank=True, max_length=500)
    average_rating = models.FloatField(verbose_name="Average Rating", blank=True, null=True)
    price = models.IntegerField(verbose_name="Price", default=0, blank=True)
    Latitude = models.CharField(verbose_name="Latitude", max_length=500, null=True, blank=True)
    Longitude  = models.CharField(verbose_name="Longitude", max_length=500, null=True, blank=True)
    
    class Meta:
        verbose_name = "Destination"
        verbose_name_plural = "Destinations"
    def __str__(self):
        return self.name


class DestinationImage(models.Model):
    created = models.DateTimeField(auto_now_add=True, verbose_name="Created")
    updated = models.DateTimeField(auto_now=True, verbose_name="Updated")
    destination = models.ForeignKey(Destination, on_delete=models.CASCADE, related_name="images")
    galery = models.CharField(verbose_name="Galery",null=True, blank=True, max_length=500)
    image = models.ImageField(verbose_name="Image",null=True, blank=True, upload_to="destination_images/")
    class Meta:
        verbose_name = "Image"
        verbose_name_plural = "Images"
    def __str__(self):
        return f"Image of {self.destination.name}"
    
class DestinationDetails(models.Model):
    created = models.DateTimeField(auto_now_add=True, verbose_name="Created")
    updated = models.DateTimeField(auto_now=True, verbose_name="Updated")
    destination = models.OneToOneField(Destination, on_delete=models.CASCADE, related_name="details")
    operating_hours = models.CharField(verbose_name="Operating Hours", max_length=200, blank=True)
    entry_fees = models.CharField(verbose_name="Entry Fees", max_length=100, blank=True)
    nearby_accommodations = models.TextField(verbose_name="Nearby Accommodations", blank=True)
    accessibility_features = models.TextField(verbose_name="Accessibility Features", blank=True)
    facilities_and_amenities = models.TextField(verbose_name="Facilities and Amenities", blank=True)
    class Meta:
        verbose_name = "Detail"
        verbose_name_plural = "Details"
    def __str__(self):
        return f"Details of {self.destination}"


class TransportationOption(models.Model):
    TRANSPORTATION_CHOICES = [
        ('Bus', 'Bus'),
        ('Train', 'Train'),
        ('Plane', 'Plane'),
        ('Car', 'Car'),
        ('Boat', 'Boat'),
        # Add more transportation options as needed
    ]
    created = models.DateTimeField(auto_now_add=True, verbose_name="Created")
    updated = models.DateTimeField(auto_now=True, verbose_name="Updated")
    destination = models.ForeignKey(Destination, verbose_name="Destination", related_name="transportation_options", on_delete=models.CASCADE)
    option = models.CharField(verbose_name="Transportation Option", max_length=20, choices=TRANSPORTATION_CHOICES)
    
    
    class Meta:
        verbose_name = "Transportation"
        verbose_name_plural = "Transportations"
    def __str__(self):
        return f"{self.option} - {self.destination}"


class DestinationAdditionalInfo(models.Model):
    created = models.DateTimeField(auto_now_add=True, verbose_name="Created")
    updated = models.DateTimeField(auto_now=True, verbose_name="Updated")
    destination = models.OneToOneField(Destination, on_delete=models.CASCADE, related_name="additional_info")
    weather_information = models.TextField(verbose_name="Weather Information", blank=True)
    historical_and_cultural_significance = models.TextField(verbose_name="Historical and Cultural Significance", blank=True)
    language_support = models.TextField(verbose_name="Language Support", blank=True)
    travel_tips_and_recommendations = models.TextField(verbose_name="Travel Tips and Recommendations", blank=True)
    social_media_links = models.TextField(verbose_name="Social Media Links", blank=True)
    class Meta:
        verbose_name = "Additional Info"
        verbose_name_plural = "Additional Info"
    def __str__(self):
        return f"Additional info for {self.destination}"