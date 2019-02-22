from locations.models import Location
from locations.serializers import LocationSerializer
from rest_framework import generics

# create generic view for handling GET and POST requests
class LocationListCreate(generics.ListCreateAPIView):
  queryset = Location.objects.all()
  serializer_class = LocationSerializer