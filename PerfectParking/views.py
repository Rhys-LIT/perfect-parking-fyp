from django.shortcuts import render
from django.http import HttpResponse

from .models import ParkingLot


class WebPages:
    HOME_PAGE = 'website/index.html'
    PARKING_LOTS = 'website/parking-lots.html'


def index(request):
    return render(request, WebPages.HOME_PAGE)


def parking_lots(request):
    parking_lots: list = ParkingLot.objects.all()
    return render(request, WebPages.PARKING_LOTS, {'parking_lots': parking_lots})
