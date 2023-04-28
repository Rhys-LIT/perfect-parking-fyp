from django import template

register = template.Library()

@register.simple_tag
def call_method(object:object , method_name: str, *args):
    method = getattr(object, method_name)
    return method(*args)

@register.simple_tag
def get_distance_from_lat_lang(parking_lot_monitor, latitude, longitude):
    return parking_lot_monitor.get_distance_from_lat_lang(latitude, longitude)
