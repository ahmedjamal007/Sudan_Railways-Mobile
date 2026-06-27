from django.urls import path

from .views import (
    ReservationListAPIView,
    ReservationCreateAPIView,
    ReservationDetailAPIView,
)

urlpatterns = [
    path("", ReservationListAPIView.as_view(), name="reservation-list"),
    path("create/", ReservationCreateAPIView.as_view(), name="reservation-create"),
    path("<uuid:pk>/", ReservationDetailAPIView.as_view(), name="reservation-detail"),
]