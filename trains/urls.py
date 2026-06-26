from django.urls import path
from .views import TrainListCreateView, TrainDetailView

urlpatterns = [
    path("", TrainListCreateView.as_view(), name="train-list-create"),
    path("<uuid:pk>/", TrainDetailView.as_view(), name="train-detail"),
]