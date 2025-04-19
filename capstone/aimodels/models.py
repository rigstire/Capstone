from django.db import models
from django.urls import reverse
from django.conf import settings

class AIModel(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField(blank=True, null=True)
    parameters = models.FloatField(blank=True, null=True)  # Number of model parameters in the millions
    created_at = models.DateTimeField(auto_now_add=True)
    qualcomm_link = models.CharField(max_length=255, unique=False)

    def __str__(self):
        return self.name
