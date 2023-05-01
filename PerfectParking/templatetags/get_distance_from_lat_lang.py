from django import template

register = template.Library()

@register.simple_tag
def call_method(object:object , method_name: str, *args):
    method = getattr(object, method_name)
    return method(*args)

@register.simple_tag
def get_distance_from_lat_lang(parking_lot_monitor, latitude, longitude):
    """Custom template tag to get the distance from a parking lot monitor to a point.

    Args:
        parking_lot_monitor (ParkingLotMonitor): The parking lot monitor to get the distance from.
        latitude (float): Latitude of the point.
        longitude (float): Longitude of the point.

    Returns:
        float : The distance from the parking lot monitor to the point.
    """
    return parking_lot_monitor.get_distance_from_lat_lang(latitude, longitude)
