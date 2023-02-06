from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import ParkingLot, ParkingLotMonitor

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']
        
class ParkingLotSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ParkingLot
        fields = ['id', 'name', 'latitude', 'longitude']

class ParkingLotMonitorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ParkingLotMonitor
        fields = ['id', 'name', 'latitude', 'longitude', 'ProbabilityParkingAvailable']