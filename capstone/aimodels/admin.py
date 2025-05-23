from django.contrib import admin
from .models import AIModel

@admin.register(AIModel)
class AIModelAdmin(admin.ModelAdmin):
    list_display = ("name", "version", "architecture", "parameters", "release_date", "created_at")
    search_fields = ("name", "version", "architecture")
    list_filter = ("architecture", "release_date")
    readonly_fields = ("created_at",)
    fieldsets = (
        ("Model Information", {
            "fields": ("name", "version", "architecture", "parameters", "description")
        }),
        ("Metadata", {
            "fields": ("release_date", "created_at")
        }),
    )

