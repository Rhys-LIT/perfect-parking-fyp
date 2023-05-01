from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import ParkingLot, ParkingLotMonitor

class UserSerializer(serializers.HyperlinkedModelSerializer):
    """
    A serializer for the User model.

    Attributes:
        None.

    Methods:
        None.
    """
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    """ this is a serializer for the Group model

    Args:
        serializers (_type_): the type of serializer
    """
    class Meta:
        model = Group
        fields = ['url', 'name']
        
class ParkingLotSerializer(serializers.HyperlinkedModelSerializer):
    """ this is a serializer for the ParkingLot model
    """
    class Meta:
        model = ParkingLot
        fields = ['id', 'name', 'latitude', 'longitude']

class ParkingLotMonitorSerializer(serializers.HyperlinkedModelSerializer):
    """this is a serializer for the ParkingLotMonitor model

    Args:
        serializers (_type_): the type of serializer
    """
    class Meta:
        """this is a serializer for the ParkingLotMonitor model
        """
        model = ParkingLotMonitor
        fields = ['id', 'name', 'latitude', 'longitude', 'probabilityParkingAvailable']