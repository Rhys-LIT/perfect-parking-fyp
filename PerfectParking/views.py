from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render

from .models import ParkingLot


class WebPages:
    HOME_PAGE = 'website/index.html'
    PARKING_LOT = 'website/parking-lot.html'
    PARKING_LOTS = 'website/parking-lots.html'
    REGISTER_USER = 'website/register.html'


def index(request):
    return render(request, WebPages.HOME_PAGE)


def parking_lots(request):
    """Builds the parking lots page. 

    Args:
        request (HttpRequest): _description_

    Returns:
        _type_: _description_
    """
    parking_lots: list = ParkingLot.objects.all()
    return render(request, WebPages.PARKING_LOTS, {'parking_lots': parking_lots})


def parking_lot(request, parking_lot_id):
    parking_lot = get_object_or_404(ParkingLot, pk=parking_lot_id)
    return render(request, WebPages.PARKING_LOT, {'parking_lot': parking_lot})

def register_user(request):
    """Guest User registers to use the app

    Args:
        request (_type_): _description_

    Returns:
        _type_: _description_
    """
    
    # load the user details from the request
    # create a new user
    
   
    return render(request, WebPages.REGISTER_USER)
