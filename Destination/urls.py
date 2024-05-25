from django.urls import path
from . import views

#step one after request
urlpatterns = [
    path('all/', views.all_destinations, name='all_destinations'),
    path('<int:idDestination>/',views.destination_details, name='details_destination'),
]