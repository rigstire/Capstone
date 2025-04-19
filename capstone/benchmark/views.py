from django.shortcuts import render
from .models import Benchmark

def benchmarks_list(request):
    benchmarks = Benchmark.objects.all()

    # Device filter
    device = request.GET.get('device')
    if device:
        benchmarks = benchmarks.filter(device__name=device)

    # Model filter
    model = request.GET.get('model')
    if model:
        benchmarks = benchmarks.filter(ai_model__name=model)

    # Dataset filter (previously input_type)
    test_dataset = request.GET.get('test_dataset')
    if test_dataset:
        benchmarks = benchmarks.filter(test_dataset=test_dataset)

    # Sorting
    sort_by = request.GET.get('sort')
    if sort_by:
        benchmarks = benchmarks.order_by(sort_by)

    # Field selection
    selected_fields = request.GET.getlist('fields')
    if not selected_fields:
        selected_fields = ['ai_model', 'device', 'test_date', 'inference_time', 'memory_usage']

    context = {
        'benchmarks': benchmarks,
        'selected_fields': selected_fields,
        'available_devices': Benchmark.objects.values_list('device__name', flat=True).distinct(),
        'available_models': Benchmark.objects.values_list('ai_model__name', flat=True).distinct(),
        'available_datasets': Benchmark.objects.values_list('test_dataset', flat=True).distinct(),
    }
    return render(request, "benchmarks_lists.html", context)

def home(request):
    return render(request, "home.html", {'hide_navbar': True})