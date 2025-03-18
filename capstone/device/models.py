from django.db import models

class Device(models.Model):
    name = models.CharField(max_length=255, unique=True)
    manufacturer = models.CharField(max_length=255, blank=True, null=True)
    chipset = models.CharField(max_length=255, blank=True, null=True)  # E.g., Snapdragon 8 Gen 2
    ram = models.PositiveIntegerField(blank=True, null=True)  # In MB
    storage = models.PositiveIntegerField(blank=True, null=True)  # In GB
    os = models.CharField(max_length=255, blank=True, null=True)  # E.g., Android 14
    release_date = models.DateField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

