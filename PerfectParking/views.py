from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import ParkingLot


class WebPages:
    HOME_PAGE = 'website/index.html'
    PARKING_LOT = 'website/parking-lot.html'
    PARKING_LOTS = 'website/parking-lots.html'
    REGISTER_USER = 'website/register-user.html'


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
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            # Save the user to the database
            user = form.save()
            # Add first name, last name, and email fields to the user model
            user.first_name = request.POST['first_name']
            user.last_name = request.POST['last_name']
            user.email = request.POST['email']
            user.save()
            return redirect('home')
    else:
        form = UserCreationForm()
   
    
    # load the user details from the request
    # create a new user
     return render(request, WebPages.REGISTER_USER, {'form': form})
   
    
