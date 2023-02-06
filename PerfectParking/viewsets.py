from django.contrib.auth.models import User, Group
from rest_framework.viewsets import ModelViewSet
from rest_framework import permissions
from .serializers import UserSerializer, GroupSerializer, ParkingLotSerializer, ParkingLotMonitorSerializer
from .models import ParkingLot, ParkingLotMonitor

class UserViewSet(ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]
    
class ParkingLotViewSet(ModelViewSet):
    """
    API endpoint that allows parking lots to be viewed or edited.
    """
    queryset = ParkingLot.objects.all()
    serializer_class = ParkingLotSerializer
    #permission_classes = [permissions.IsAuthenticated]
    
class ParkingLotMonitorViewSet(ModelViewSet):
    """
    API endpoint that allows parking lot monitors to be viewed or edited.
    """
    queryset = ParkingLotMonitor.objects.all()
    serializer_class = ParkingLotMonitorSerializer
    #permission_classes = [permissions.IsAuthenticated]