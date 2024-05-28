from django.shortcuts import get_object_or_404, render
from .models import Destination, DestinationDetails,DestinationImage, TransportationOption
from utils import helpers
# Create your views here.
def all_destinations(request):
    destinations = Destination.objects.all().order_by('created')
    companyInfo = helpers.getCompanyInfo()
    city_names = Destination.objects.all().order_by('created').values('location').distinct()
    # Handle form submission
    if request.method == 'GET':
      
        destination_id = request.GET.get('location')
        special_budget = request.GET.get('special_budget')
        print(destination_id)
        # Filter destinations based on form inputs
        if destination_id:
            print('dafasdfasdfasdfasdf')
            print(destination_id)
            destinations = destinations.filter(location=destination_id )

        if special_budget and special_budget != 'none' and special_budget != 'all':
            min_budget, max_budget = map(int, special_budget.split('-'))
            
            # Filter destinations within the specified budget range
            destinations = destinations.filter(price__range=(min_budget, max_budget))

    context = {
        'companyInfo': companyInfo,
        'destinations': destinations,
        'city_names':city_names
    }
    return render(request, 'destinations.html', context)


def destination_details(request,idDestination):
    destination = get_object_or_404(Destination, pk=idDestination)
    detailsDestination = DestinationDetails.objects.get(destination=destination)
    imageDestination = DestinationImage.objects.filter(destination=destination)
    transportationOption = TransportationOption.objects.filter(destination=destination)
 

    companyInfo = helpers.getCompanyInfo()
    context = {
        'destination': destination,
        'latitude': destination.Latitude,
        'longitude':destination.Longitude,
        'companyInfo':companyInfo,
        'images':imageDestination,
        'detailsDestination':detailsDestination,
        'transportationOption':transportationOption
         
    }
    return render(request, 'detail-destination.html', context)

