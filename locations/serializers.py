from rest_framework import serializers
from locations.models import Location

class LocationSerializer(serializers.ModelSerializer):
  class Meta:
    model = Location
    # fields = "__all__"
    # can explicitly add the fields needed if not all are supposed to be included
    fields = (
      'id',
      'street_number', 
      'locality', 
      'latitude',
      'longitude',
      'accessibility',
      'price_per_week', 
      'max_guests',
      'num_bathrooms',
      'air_conditioning',
      'wifi'
    )
