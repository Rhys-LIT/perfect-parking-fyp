""" PerfectParking URL Configuration"""
from django.urls import path
from . import views, WebPaths

urlpatterns = [
    path(WebPaths.ROOT, views.index, name='home'),
    path('logout-user/', views.logout_user, name='logout-user'),
    path(WebPaths.PARKING_LOTS, views.parking_lots, name='parking-lots'),
    path(f'{WebPaths.PARKING_LOTS}/<int:parking_lot_id>', views.parking_lot, name='parking-lot'),
    path(WebPaths.REGISTER_USER, views.register_user, name='register-user'),
    path(WebPaths.PARKING_LOT_MONITORS, views.parking_lot_monitors, name='parking-lot-monitors'),
    path(f'{WebPaths.PARKING_LOT_MONITOR}/<int:parking_lot_monitor_id>', views.parking_lot_monitor, name='parking-lot-monitor'),
]