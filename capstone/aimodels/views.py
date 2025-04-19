from django.shortcuts import render, get_object_or_404
from .models import AIModel
from  device.models import Device
from benchmark.models import Benchmark

def ai_models_list(request):
     return render(request, "ai_models_list.html", {"ai_models": AIModel.objects.all()})

def ai_model_detail(request, ai_model_id):
    ai_model = get_object_or_404(AIModel, id=ai_model_id)
    return render(request, "ai_model_detail.html", {"ai_model": ai_model})

def compare_models(request): 
    model_a_id = request.GET.get('model_a')
    model_b_id = request.GET.get('model_b')
    device_a_id = request.GET.get('device_a')
    device_b_id = request.GET.get('device_b')

    model_a = AIModel.objects.filter(id=model_a_id).first() if model_a_id else None
    model_b = AIModel.objects.filter(id=model_b_id).first() if model_b_id else None
    device_a = Device.objects.filter(id=device_a_id).first() if device_a_id else None
    device_b = Device.objects.filter(id=device_b_id).first() if device_b_id else None

    benchmark_a = Benchmark.objects.filter(ai_model=model_a, device=device_a).order_by('-test_date').first() if model_a and device_a else None
    benchmark_b = Benchmark.objects.filter(ai_model=model_b, device=device_b).order_by('-test_date').first() if model_b and device_b else None

    all_models = AIModel.objects.all()
    all_devices = Device.objects.all()

    return render(request, 'model_comparison.html', {
        'model_a': model_a,
        'model_b': model_b,
        'device_a': device_a,
        'device_b': device_b,
        'benchmark_a': benchmark_a,
        'benchmark_b': benchmark_b,
        'all_models': all_models,
        'all_devices': all_devices,
    })