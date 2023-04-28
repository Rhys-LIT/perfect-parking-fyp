import random
from django.db import models
from haversine import haversine
# Create your models here.
class ParkingLot(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, unique=True)
    address = models.CharField(max_length=255)
    hours = models.CharField(max_length=255)
    isPaidParking = models.BooleanField(default=True)
    latitude = models.DecimalField(max_digits=17, decimal_places=15)
    longitude = models.DecimalField(max_digits=17, decimal_places=15)
    image = models.ImageField(upload_to='images/parking-lot/', blank=True)
    parking_spaces = models.IntegerField(default=1)
    
    def __str__(self):
        return self.name
    
class ParkingLotMonitor(models.Model):
    id = models.AutoField(primary_key=True)
    parkingLot = models.ForeignKey(ParkingLot, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, unique=True)
    """The name of the parking lot monitor.
    This is the name that will be displayed to the user.
    Max length is 100 characters."""
    latitude = models.DecimalField(max_digits=17, decimal_places=15)
    """The latitude of the parking lot monitor"""
    longitude = models.DecimalField(max_digits=17, decimal_places=15)
    """The longitude of the parking lot monitor"""
    probabilityParkingAvailable = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    """The probability that the parking lot is available."""
    free_parking_spaces = models.IntegerField(default=0)
    dateTimeLastUpdated = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)
    """status: True = online, False = offline"""
    image = models.ImageField(upload_to='images/parking-lot-monitor/', blank=True)
    
    def get_distance_from_lat_lang(self, latitude: float, longitude: float) -> float:
        return self.get_distance_from_point((latitude, longitude))
    
    def get_distance_from_point(self, user_point: tuple) -> float:
        """Gets the distance in Kilometers from the user GPS coordinates to the parking lot coordinates.

        Returns:
            float: The distance in Kilometers from the user GPS coordinates to the parking lot coordinates.
        """
        return haversine(self.get_gps_point(), user_point)
    
    def get_gps_point(self) -> tuple:
        """Gets the GPS coordinates of the parking lot.

        Returns:
            tuple: The GPS coordinates of the parking lot.
        """
        return (self.latitude, self.longitude)
    
    def __str__(self):
        return self.name