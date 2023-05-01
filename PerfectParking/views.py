from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import ParkingLot, ParkingLotMonitor
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect
from django.views import generic
from django.contrib.auth import logout
from django.urls import reverse

from django.urls import reverse_lazy
from . import WebPaths


class WebPages:
    HOME_PAGE = "website/index.html"
    PARKING_LOT = "website/parking-lot.html"
    PARKING_LOT_MONITOR = "website/parking-lot-monitor.html"
    PARKING_LOT_MONITORS = "website/parking-lot-monitors.html"
    PARKING_LOTS = "website/parking-lots.html"
    REGISTER_USER = "website/register-user.html"
    LOGIN_USER = "website/login-user.html"


def index(request):
    return render(request, WebPages.HOME_PAGE)


def login_user(request):
    """
    Authenticates and logs in a user based on their submitted username and password.

    Args:
        request: An HttpRequest object that contains metadata about the current request.

    Returns:
        If the submitted form data is valid and the user exists, redirects to the parking lots page. Otherwise,
        redirects to the login page.

    Raises:
        None
    """
    if request.method == "POST":  # FORM SUBMITTED
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect(WebPaths.PARKING_LOTS)
        else:
            return redirect(WebPaths.LOGIN)
    else:  # FORM NOT SUBMITTED
        form = AuthenticationForm()
        return render(request, "registration/login.html", {"form": form})


def logout_user(request):
    logout(request)
    return redirect(WebPages.HOME_PAGE)


def parking_lot(request, parking_lot_id):
    parking_lot = get_object_or_404(ParkingLot, pk=parking_lot_id)
    return render(request, WebPages.PARKING_LOT, {"parking_lot": parking_lot})


def parking_lots(request):
    """Builds the parking lots page.

    Args:
        request (HttpRequest): _description_

    Returns:
        _type_: _description_
    """
    parking_lots: list = ParkingLot.objects.all()
    return render(request, WebPages.PARKING_LOTS, {"parking_lots": parking_lots})


def parking_lot_monitor(request, parking_lot_monitor_id):
    parking_lot_monitor = get_object_or_404(
        ParkingLotMonitor, pk=parking_lot_monitor_id
    )
    return render(
        request,
        WebPages.PARKING_LOT_MONITOR,
        {"parking_lot_monitor": parking_lot_monitor},
    )


def parking_lot_monitors(request):
    """Builds the parking lot monitors page.

    Args:
        request (HttpRequest): _description_

    Returns:
        _type_: _description_
    """
    parking_lot_monitors: list = ParkingLotMonitor.objects.all()

    if request.method == "POST":  # FORM SUBMITTED
        latitude = request.POST["latitude"]
        longitude = request.POST["longitude"]

        context = {
            "parking_lot_monitors": parking_lot_monitors,
            "user_point": {"latitude": latitude, "longitude": longitude},
        }
        return render(request, WebPages.PARKING_LOT_MONITORS, context)

    return render(
        request,
        WebPages.PARKING_LOT_MONITORS,
        {"parking_lot_monitors": parking_lot_monitors},
    )


def register_user(request):
    """Guest User registers to use the app

    Args:
        request (_type_): _description_

    Returns:
        _type_: _description_
    """
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            # Save the user to the database
            user = form.save()
            # Add first name, last name, and email fields to the user model
            user.first_name = request.POST["first_name"]
            user.last_name = request.POST["last_name"]
            user.email = request.POST["email"]
            user.save()
            return redirect(WebPaths.LOGIN)
    else:
        form = UserCreationForm()
    return render(request, WebPages.REGISTER_USER, {"form": form})

    # load the user details from the request
    # create a new user
