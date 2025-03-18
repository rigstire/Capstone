from django.contrib import admin
from .models import Benchmark

@admin.register(Benchmark)
class BenchmarkAdmin(admin.ModelAdmin):
    list_display = ("ai_model", "device", "test_date", "inference_time", "accuracy", "power_consumption")
    search_fields = ("ai_model__name", "device__name")
    list_filter = ("test_date", "ai_model", "device")
    readonly_fields = ("test_date",)
    fieldsets = (
        ("Benchmark Details", {
            "fields": ("ai_model", "device", "inference_time", "accuracy", "power_consumption", "notes")
        }),
        ("Test Information", {
            "fields": ("test_date",)
        }),
    )