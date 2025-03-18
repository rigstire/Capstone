from django.shortcuts import render, get_object_or_404
from .models import  Device

def devices_list(request):
    return render(request, "devices_list.html", {"devices": Device.objects.all()})

def devices_detail(request, device_id):
    device = get_object_or_404(Device, id=device_id)
    return render(request, "devices_detail.html", {"device": device})
