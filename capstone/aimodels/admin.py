from django.contrib import admin
from .models import AIModel

@admin.register(AIModel)
class AIModelAdmin(admin.ModelAdmin):
    list_display = ("name", "parameters", "accuracy", "description")
    search_fields = ("name", "runtime", "architecture")
    readonly_fields = ("created_at",)
    fieldsets = (
        ("Model Information", {
            "fields": ("name", "parameters", "accuracy","description")
        }),

    )

