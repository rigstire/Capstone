from django.shortcuts import render, get_object_or_404
from .models import  Device

def devices_list(request):
    devices = Device.objects.all().order_by('manufacturer', 'name')
    return render(request, "devices_list.html", {"devices": devices})

def devices_detail(request, device_id):
    device = get_object_or_404(Device, id=device_id)
    benchmarks = device.benchmarks.all()
    
    # Handle sorting
    sort_by = request.GET.get('sort', '')
    if sort_by == 'inference_time':
        benchmarks = benchmarks.order_by('inference_time')
    elif sort_by == '-accuracy':
        benchmarks = benchmarks.order_by('-accuracy')
    
    context = {
        'device': device,
        'benchmarks': benchmarks,
    }
    return render(request, 'devices_detail.html', context)
