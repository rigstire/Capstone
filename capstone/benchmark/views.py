from django.shortcuts import render
from .models import Benchmark

def benchmarks_list(request):
    # Initialize base queryset
    benchmarks = Benchmark.objects.all()
    
    # Get filter parameters from request
    device = request.GET.get('device')
    model = request.GET.get('model')
    test_dataset = request.GET.get('test_dataset')
    sort_by = request.GET.get('sort')
    
    # Apply filters
    if device:
        benchmarks = benchmarks.filter(device__name=device)
    if model:
        benchmarks = benchmarks.filter(ai_model__name=model)
    if test_dataset:
        benchmarks = benchmarks.filter(test_dataset=test_dataset)
    
    # Apply sorting
    if sort_by:
        benchmarks = benchmarks.order_by(sort_by)
    
    # Handle field selection
    selected_fields = request.GET.getlist('fields', [
        'ai_model', 
        'device', 
        'test_date', 
        'inference_time', 
        'accuracy', 
        'memory_usage'
    ])
    
    # Get top performers based on current filters and sort
    top_performers = benchmarks[:3] if sort_by else benchmarks.order_by('inference_time')[:3]
    
    context = {
        'benchmarks': benchmarks,
        'selected_fields': selected_fields,
        'available_devices': Benchmark.objects.values_list('device__name', flat=True).distinct(),
        'available_models': Benchmark.objects.values_list('ai_model__name', flat=True).distinct(),
        'available_datasets': Benchmark.objects.values_list('test_dataset', flat=True).distinct(),
        'top_performers': top_performers,
        'current_sort': sort_by
    }
    
    return render(request, "benchmarks_lists.html", context)

def home(request):
    return render(request, "home.html", {'hide_navbar': True})