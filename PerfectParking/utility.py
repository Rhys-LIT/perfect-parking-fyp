""" Utility for the PerfectParking project"""
from django.contrib.auth.models import User
from .models import ParkingLotMonitor, ParkingRequestLog

def build_all_config_ini_content() -> str:
    """
    Builds a string containing the configuration content for all parking lot monitors.

    Returns:
        A string containing the configuration content for all parking lot monitors.
    """
    text: str = ""
    parking_lot_monitors: list(ParkingLotMonitor) = ParkingLotMonitor.objects.all()
    for parking_lot_monitor in parking_lot_monitors:
        text += build_config_ini_content(parking_lot_monitor)+"\n\n"
    return text


def build_config_ini_content(parking_lot_monitor: ParkingLotMonitor) -> str:
    """Builds the content of the config.ini file.

    Args:
        parking_lot_monitor (ParkingLotMonitor): The parking lot monitor to build the config.ini file for.

    Returns:
        str: The content of the config.ini file.
    """
    return f"""[ParkingLotMonitor]
Id={parking_lot_monitor.id}
Name={parking_lot_monitor.name}
Latitude={parking_lot_monitor.latitude}
Longitude={parking_lot_monitor.longitude}
ParkingSpaces={parking_lot_monitor.parkingLot.parking_spaces}

[App]
Token=0f412f508358b8c1156d688d1db671e5ba4f1457
Username=parkingMonitor
Password=Letmein1$
ServerUrl=http://127.0.0.1:8000/api-auth/parking-lot-monitors"""

def record_user_query(area_of_interest_latitude, area_of_interest_longitude, request):
    """Records a user query in the database.

    Args:
        latitude (float): The latitude of the user query.
        longitude (float): The longitude of the user query.
    """

    parking_request_log:ParkingRequestLog = ParkingRequestLog()
    parking_request_log.area_of_interest_latitude = area_of_interest_latitude
    parking_request_log.area_of_interest_longitude = area_of_interest_longitude
    parking_request_log.user = User.objects.get(username=request.user.username)
    parking_request_log.user_ip_address = request.META.get("REMOTE_ADDR")

    parking_request_log.save()
