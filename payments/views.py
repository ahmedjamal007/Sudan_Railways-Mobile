from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from .models import Payment
from .serializers import PaymentSerializer


class PaymentListAPIView(generics.ListAPIView):
    serializer_class = PaymentSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return (
            Payment.objects
            .select_related(
                "reservation",
                "reservation__schedule",
                "reservation__schedule__train",
                "reservation__schedule__departure_station",
                "reservation__schedule__arrival_station",
            )
            .filter(reservation__user=self.request.user)
            .order_by("-created_at")
        )


class PaymentCreateAPIView(generics.CreateAPIView):
    serializer_class = PaymentSerializer
    permission_classes = [IsAuthenticated]


class PaymentDetailAPIView(generics.RetrieveAPIView):
    serializer_class = PaymentSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return (
            Payment.objects
            .select_related(
                "reservation",
                "reservation__schedule",
                "reservation__schedule__train",
                "reservation__schedule__departure_station",
                "reservation__schedule__arrival_station",
            )
            .filter(reservation__user=self.request.user)
        )