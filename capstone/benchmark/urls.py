from django.urls import path
from . import views

urlpatterns = [
      path("benchmarks/", views.benchmarks_list, name="benchmarks_list"),
      path("",views.home, name="home")
]