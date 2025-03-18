from django.shortcuts import render, get_object_or_404
from .models import AIModel

def ai_models_list(request):
     return render(request, "ai_models_list.html", {"ai_models": AIModel.objects.all()})

def ai_model_detail(request, ai_model_id):
    ai_model = get_object_or_404(AIModel, id=ai_model_id)
    return render(request, "ai_model_detail.html", {"ai_model": ai_model})