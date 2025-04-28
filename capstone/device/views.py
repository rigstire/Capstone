from django.shortcuts import render, get_object_or_404
from .models import Device

def devices_list(request):
    devices = Device.objects.all().order_by('manufacturer', 'name')
    return render(request, "devices_list.html", {"devices": devices})

def devices_detail(request, device_id):
    device = get_object_or_404(Device, id=device_id)
    benchmarks = device.benchmarks.all()
    
    # Get unique test datasets for the filter dropdown
    unique_datasets = benchmarks.order_by('test_dataset').values_list('test_dataset', flat=True).distinct()
    
    # Handle dataset filtering
    test_dataset = request.GET.get('test_dataset')
    if test_dataset:
        benchmarks = benchmarks.filter(test_dataset=test_dataset)
    
    # Handle sorting
    sort_by = request.GET.get('sort', '')
    if sort_by == 'inference_time':
        benchmarks = benchmarks.order_by('inference_time')
    elif sort_by == '-accuracy':
        benchmarks = benchmarks.order_by('-accuracy')
    
    context = {
        'device': device,
        'benchmarks': benchmarks,
        'unique_datasets': unique_datasets,
    }
    return render(request, 'devices_detail.html', context)