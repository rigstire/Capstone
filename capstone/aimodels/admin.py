from django.contrib import admin
from .models import AIModel

@admin.register(AIModel)
class AIModelAdmin(admin.ModelAdmin):
    list_display = ("name", "parameters", "created_at")
    search_fields = ("name",)
    list_filter = ( "accuracy",)
    readonly_fields = ("created_at",)
    fieldsets = (
        ("Model Information", {
            "fields": ("name", "parameters", "description", "accuracy")
        }),
        ("Metadata", {
            "fields": ( "created_at",)
        }),
    )

