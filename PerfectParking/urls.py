from django.urls import path

from . import views

class WebPaths:
    ROOT = ''
    PARKING_LOTS = 'parking-lots'
    

urlpatterns = [
    path(WebPaths.ROOT, views.index, name='index'),
    path(WebPaths.PARKING_LOTS, views.parking_lots, name='parking-lots'),
]