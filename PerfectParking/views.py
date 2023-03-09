from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import ParkingLot
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect


class WebPages:
    HOME_PAGE = 'website/index.html'
    PARKING_LOT = 'website/parking-lot.html'
    PARKING_LOTS = 'website/parking-lots.html'
    REGISTER_USER = 'website/register-user.html'
    LOGIN_USER = 'website/login-user.html'


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

def login_user(request):
    """Logs the user in

    Args:
        request (_type_): _description_

    Returns:
        _type_: _description_
    """
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            # login the user
            user = form.get_user()
            login(request, user)
            return redirect('parking-lots')
    else:
        form = AuthenticationForm()
    return render(request, WebPages.LOGIN_USER, {'form': form})

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
            return redirect('parking-lots')
    else:
        form = UserCreationForm()
    return render(request, WebPages.REGISTER_USER, {'form': form})

   
  
    
    # load the user details from the request
    # create a new user
    
   
    
