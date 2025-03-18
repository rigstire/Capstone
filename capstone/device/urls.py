from django.urls import path
from . import views

urlpatterns = [
    path("devices/", views.devices_list, name="devices_list"),
       path("devices/<int:device_id>/", views.devices_detail, name="device_detail"),
]