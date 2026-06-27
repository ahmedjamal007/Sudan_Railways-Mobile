from django.urls import path

from .views import (
    PaymentListAPIView,
    PaymentCreateAPIView,
    PaymentDetailAPIView,
)

urlpatterns = [
    path("", PaymentListAPIView.as_view(), name="payment-list"),
    path("create/", PaymentCreateAPIView.as_view(), name="payment-create"),
    path("<uuid:pk>/", PaymentDetailAPIView.as_view(), name="payment-detail"),
]