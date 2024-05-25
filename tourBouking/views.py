from django.shortcuts import render, redirect
from datetime import datetime
from utils import helpers
from .models import TourBooking
from Destination.models import Destination


def add_tour_booking(request):
    companyInfo= helpers.getCompanyInfo()
    destinations = Destination.objects.all()
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        date_time = datetime.now()
        destination = request.POST.get('destination')
        number_of_persons = request.POST.get('number_of_persons')
        number_of_kids = request.POST.get('number_of_kids')
        special_request = request.POST.get('special_request')
        special_accommodation=request.POST.get('special_accommodation')
        destinationSelected =  Destination.objects.get(id=destination)
        booking = TourBooking(
            name=name,
            email=email,
            phone=phone,
            date_time=date_time,
            destination=destinationSelected,
            number_of_persons=number_of_persons,
            number_of_kids=number_of_kids,
            special_request=special_request,
            special_accommodation=special_accommodation,
        )

        booking.save()
        return redirect('success_booking', booking_id=booking.id)
    else:
        context={
        "companyInfo" : companyInfo,
        "destinations": destinations
    }
        return render(request, 'findAnimal.html',context)
    

def booking_success(request, booking_id):
    booking = TourBooking.objects.get(id=booking_id)
    context = {
        'name': booking.name,
        'email': booking.email,
        'date_time': booking.date_time,
        'destination': booking.destination,
        'number_of_persons': booking.number_of_persons,
        'special_request': booking.special_request,
        'special_accommodation': booking.special_accommodation,
        "companyInfo" : helpers.getCompanyInfo()
    }     
    return render(request,'success_booking.html',context)