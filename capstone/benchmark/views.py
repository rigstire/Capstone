from django.shortcuts import render
from .models import Benchmark

def benchmarks_list(request):
    benchmarks = Benchmark.objects.all()
    return render(request, "benchmarks_lists.html", {"benchmarks": benchmarks})  # ✅ Ensure correct path
