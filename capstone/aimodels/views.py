from django.shortcuts import render, get_object_or_404
from .models import AIModel
from  device.models import Device
from benchmark.models import Benchmark

def ai_models_list(request):
    # Get large models (>30M parameters)
    large_models = AIModel.objects.filter(parameters__gt=30).order_by('name')
    
    # Get small models (<=30M parameters)
    small_models = AIModel.objects.filter(parameters__lte=30).order_by('name')
    
    context = {
        'large_models': large_models,
        'small_models': small_models,
    }
    return render(request, "ai_models_list.html", context)

def ai_model_detail(request, ai_model_id):
    ai_model = get_object_or_404(AIModel, id=ai_model_id)
    
    # Get all benchmarks related to this model
    benchmarks = ai_model.benchmarks.all()
    
    # Filter by test dataset if selected
    test_dataset = request.GET.get('test_dataset')
    if test_dataset:
        benchmarks = benchmarks.filter(test_dataset=test_dataset)
    
    # Handle sorting
    sort_by = request.GET.get('sort', '')
    if sort_by == 'inference_time':
        benchmarks = benchmarks.order_by('inference_time')  # Fastest first
    elif sort_by == '-accuracy':
        benchmarks = benchmarks.order_by('-accuracy')  # Highest accuracy first
    
    # Get unique dataset values for the dropdown
    unique_datasets = ai_model.benchmarks.values_list('test_dataset', flat=True).distinct()

    context = {
        'ai_model': ai_model,
        'benchmarks': benchmarks,
        'unique_datasets': unique_datasets,
    }
    return render(request, "ai_model_detail.html", context)


from django.shortcuts import render
from .models import AIModel
from device.models import Device
from benchmark.models import Benchmark

def compare_models(request): 
    model_a_id = request.GET.get('model_a')
    model_b_id = request.GET.get('model_b')
    device_a_id = request.GET.get('device_a')
    device_b_id = request.GET.get('device_b')
    test_dataset = request.GET.get('test_dataset')

    if not test_dataset:
        return render(request, 'model_comparison.html', {
            'error': 'Please select a test dataset.',
            'all_models': AIModel.objects.all(),
            'all_devices': Device.objects.all(),
            'all_test_datasets': Benchmark.objects.values_list('test_dataset', flat=True).distinct(),
        })

    model_a = AIModel.objects.filter(id=model_a_id).first() if model_a_id else None
    model_b = AIModel.objects.filter(id=model_b_id).first() if model_b_id else None
    device_a = Device.objects.filter(id=device_a_id).first() if device_a_id else None
    device_b = Device.objects.filter(id=device_b_id).first() if device_b_id else None

    filters = {'test_dataset': test_dataset}

    benchmark_a = Benchmark.objects.filter(ai_model=model_a, device=device_a, **filters).order_by('-test_date').first() if model_a and device_a else None
    benchmark_b = Benchmark.objects.filter(ai_model=model_b, device=device_b, **filters).order_by('-test_date').first() if model_b and device_b else None

    return render(request, 'model_comparison.html', {
        'model_a': model_a,
        'model_b': model_b,
        'device_a': device_a,
        'device_b': device_b,
        'benchmark_a': benchmark_a,
        'benchmark_b': benchmark_b,
        'all_models': AIModel.objects.all(),
        'all_devices': Device.objects.all(),
        'all_test_datasets': Benchmark.objects.values_list('test_dataset', flat=True).distinct(),
        'selected_dataset': test_dataset,
    })
