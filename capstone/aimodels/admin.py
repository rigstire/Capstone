from django.contrib import admin
from .models import AIModel

@admin.register(AIModel)
class AIModelAdmin(admin.ModelAdmin):
    list_display = ("name", "parameters", "description","qualcomm_link")
    search_fields = ("name", "runtime", "architecture","qualcomm_link")
    readonly_fields = ("created_at",)
    fieldsets = (
        ("Model Information", {
            "fields": ("name", "parameters","description","qualcomm_link")
        }),

    )

