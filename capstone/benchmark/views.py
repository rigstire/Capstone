from django.shortcuts import render
from .models import Benchmark

# Define allowed sort fields
ALLOWED_SORT_FIELDS = {
    'inference_time': 'Inference Time (Low to High)',
    '-inference_time': 'Inference Time (High to Low)',
    '-accuracy': 'Accuracy (High to Low)',  # Note: We use -accuracy for high-to-low
    'accuracy': 'Accuracy (Low to High)',
    'memory_usage': 'Memory Usage (Low to High)',
    '-memory_usage': 'Memory Usage (High to Low)',
}

def benchmarks_list(request):
    # Initialize base queryset
    benchmarks = Benchmark.objects.all()
    
    # Get filter parameters from request
    device = request.GET.get('device')
    model = request.GET.get('model')
    test_dataset = request.GET.get('test_dataset')
    sort_by = request.GET.get('sort', 'inference_time')  # Default to fastest inference

    # Apply filters
    if device:
        benchmarks = benchmarks.filter(device__name=device)
    if model:
        benchmarks = benchmarks.filter(ai_model__name=model)
    if test_dataset:
        benchmarks = benchmarks.filter(test_dataset=test_dataset)

    # Handle accuracy sorting specially (we want high-to-low by default)
    if sort_by == 'accuracy':
        # User selected "Accuracy (Low to High)" from dropdown
        benchmarks = benchmarks.order_by('accuracy')
    elif sort_by == '-accuracy':
        # User selected "Accuracy (High to Low)" from dropdown
        benchmarks = benchmarks.order_by('-accuracy')
    elif sort_by in ALLOWED_SORT_FIELDS:
        # For all other fields, use the sort directly
        benchmarks = benchmarks.order_by(sort_by)
    else:
        benchmarks = benchmarks.order_by('inference_time')  # Fallback to default

    # Get top performers using the same sorting
    top_performers = benchmarks[:3]
    
    # Determine the primary metric being sorted
    sort_field = sort_by.lstrip('-')
    
    # Handle field selection
    selected_fields = request.GET.getlist('fields', [
        'ai_model', 
        'device', 
        'test_date', 
        'inference_time', 
        'accuracy', 
        'memory_usage'
    ])

    context = {
        'benchmarks': benchmarks,
        'top_performers': top_performers,
        'selected_fields': selected_fields,
        'available_devices': Benchmark.objects.values_list('device__name', flat=True).distinct(),
        'available_models': Benchmark.objects.values_list('ai_model__name', flat=True).distinct(),
        'available_datasets': Benchmark.objects.values_list('test_dataset', flat=True).distinct(),
        'current_sort': sort_by,
        'sort_label': ALLOWED_SORT_FIELDS.get(sort_by, 'Inference Time (Low to High)'),
        'sort_field': sort_field,
        'available_sort_fields': ALLOWED_SORT_FIELDS,
    }

    return render(request, "benchmarks_lists.html", context)

def home(request):
    return render(request, "home.html", {'hide_navbar': True})