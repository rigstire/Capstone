from django.db import models
from django.urls import reverse
from django.conf import settings

class AIModel(models.Model):
    name = models.CharField(max_length=255, unique=True)
    runtime = models.CharField(max_length=50, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    release_date = models.DateField(blank=True, null=True)
    parameters = models.PositiveIntegerField(blank=True, null=True)  # Number of model parameters
    architecture = models.CharField(max_length=255, blank=True, null=True)  # E.g., Transformer, CNN, RNN
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} {self.version}"
