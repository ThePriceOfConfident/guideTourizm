
from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static
from tourBouking.views import add_tour_booking
from tourBouking.views import booking_success
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('tourizmConfig.urls')),
    path('', include('tourBouking.urls')),
    path('traveler/', include('traveler.urls')),
    path('destination/', include('Destination.urls')),
    path( "markers/", include("localisation.urls"),  ),
   
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    
admin.site.site_header = "TOURIZMO Admin"
admin.site.site_title = "TOURIZMO Admin Portal"
admin.site.index_title = "Welcome to TOURIZMO Trip Portal"