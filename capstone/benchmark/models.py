from django.db import models
from django.apps import apps

# Create your models here.
class Benchmark(models.Model):
    ai_model = models.ForeignKey('aimodels.AIModel', on_delete=models.CASCADE, related_name="benchmarks")
    device = models.ForeignKey('device.Device', on_delete=models.CASCADE, related_name="benchmarks")
    test_date = models.DateField(auto_now_add=True)
    inference_time = models.FloatField(help_text="Time in milliseconds")  # Lower is better
    accuracy = models.FloatField(help_text="Accuracy as a percentage")  # E.g., 95.3 for 95.3%
    power_consumption = models.FloatField(blank=True, null=True, help_text="Power used in watts")
    notes = models.TextField(blank=True, null=True)

    class Meta:
        unique_together = ("ai_model", "device", "test_date")  # Prevent duplicate entries

    def __str__(self):
        return f"{self.ai_model} on {self.device} - {self.test_date}"
