from django.urls import path
from . import views

urlpatterns = [
    path("ai-models/", views.ai_models_list, name="ai_models_list"),
    path("ai-models/<int:ai_model_id>/", views.ai_model_detail, name="ai_model_detail"),
    path("ai-models/compare_models/", views.compare_models, name="compare_models")
]