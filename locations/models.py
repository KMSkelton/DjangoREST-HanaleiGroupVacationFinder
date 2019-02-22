from django.db import models
from locality.models import Locality

class Location(models.Model):
    street_number = models.CharField(max_length=20, blank=True)
    route = models.CharField(max_length=100, blank=True)
    locality = models.ForeignKey(Locality, on_delete=models.CASCADE, related_name='addresses', blank=True, null=True)
    raw = models.CharField(max_length=200)
    formatted = models.CharField(max_length=200, blank=True)
    latitude = models.FloatField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)
    accessibility = models.NullBooleanField(blank=True, null=True)
    price_per_week = models.FloatField(blank=True, null=True)
    max_guests = models.IntegerField(blank=True, null=True)
    num_bathrooms = models.IntegerField(blank=True, null=True)
    air_conditioning = models.NullBooleanField(blank=True, null=True)
    wifi = models.NullBooleanField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)