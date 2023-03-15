from django.urls import include, path
from . import WebPaths
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path(WebPaths.ROOT, views.index, name='index'),
    path('logout-user/', views.logout_user, name='logout-user'),
    path(WebPaths.PARKING_LOTS, views.parking_lots, name='parking-lots'),
    path(f'{WebPaths.PARKING_LOTS}/<int:parking_lot_id>', views.parking_lot, name='parking-lot'),
    path(WebPaths.REGISTER_USER, views.register_user, name='register-user'),
]