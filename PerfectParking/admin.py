from django.contrib import admin

from PerfectParking.models import ParkingLot, ParkingLotMonitor

# Register your models here.

admin.site.register(ParkingLot)
admin.site.register(ParkingLotMonitor)
