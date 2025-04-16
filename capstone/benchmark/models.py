from django.db import models
from django.apps import apps

# Create your models here.
class Benchmark(models.Model):
    ai_model = models.ForeignKey('aimodels.AIModel', on_delete=models.CASCADE, related_name="benchmarks")
    device = models.ForeignKey('device.Device', on_delete=models.CASCADE, related_name="benchmarks")
    test_date = models.DateField(auto_now_add=True)
    runtime = models.CharField(blank=True,null=True, max_length=50000)
    inference_time = models.FloatField(help_text="Time in milliseconds")  # Lower is better
    memory_usage = models.FloatField(blank=True, null=True, help_text="Power used in watts")
    compute_units = models.FloatField(blank=True, null= True, help_text="Number of compute units used for image processing")
    notes = models.TextField(blank=True, null=True)

    class Meta:
        unique_together = ("ai_model", "device", "test_date")  # Prevent duplicate entries

    def __str__(self):
        return f"{self.ai_model} on {self.device} - {self.test_date}"
