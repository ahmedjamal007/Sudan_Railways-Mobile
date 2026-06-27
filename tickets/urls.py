from django.urls import path

from .views import (
    TicketListAPIView,
    TicketDetailAPIView,
)

urlpatterns = [
    path("", TicketListAPIView.as_view(), name="ticket-list"),
    path("<uuid:pk>/", TicketDetailAPIView.as_view(), name="ticket-detail"),
]