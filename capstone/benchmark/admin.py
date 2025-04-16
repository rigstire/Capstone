from django.contrib import admin
from .models import Benchmark
from import_export import resources
from import_export.admin import ImportExportModelAdmin

@admin.register(Benchmark)
class BenchmarkAdmin(admin.ModelAdmin):
    list_display = ("ai_model", "device","runtime" ,"test_date", "inference_time", "memory_usage", "compute_units")
    search_fields = ("ai_model__name", "device__name")
    list_filter = ("test_date", "ai_model", "device")
    readonly_fields = ("test_date",)
    fieldsets = (
        ("Benchmark Details", {
            "fields": ("ai_model", "device","runtime" ,"inference_time", "memory_usage", "compute_units", "notes")
        }),
        ("Test Information", {
            "fields": ("test_date",)
        }),
    )
