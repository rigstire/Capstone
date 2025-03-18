from django.contrib import admin
from .models import Device

@admin.register(Device)
class DeviceAdmin(admin.ModelAdmin):
    list_display = ("name", "manufacturer", "chipset", "ram", "storage", "os", "release_date", "created_at")
    search_fields = ("name", "manufacturer", "chipset", "os")
    list_filter = ("manufacturer", "os", "release_date")
    readonly_fields = ("created_at",)
    fieldsets = (
        ("Device Specifications", {
            "fields": ("name", "manufacturer", "chipset", "ram", "storage", "os")
        }),
        ("Metadata", {
            "fields": ("release_date", "created_at")
        }),
    )
