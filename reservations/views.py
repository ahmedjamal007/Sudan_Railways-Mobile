from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from .models import Reservation
from .serializers import ReservationSerializer

class ReservationListAPIView(generics.ListAPIView):
    serializer_class = ReservationSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return (
            Reservation.objects
            .select_related(
                "schedule",
                "schedule__train",
                "schedule__departure_station",
                "schedule__arrival_station",
            )
            .filter(user=self.request.user)
            .order_by("-created_at")
        )

class ReservationCreateAPIView(generics.CreateAPIView):
    serializer_class = ReservationSerializer
    permission_classes = [IsAuthenticated]

class ReservationDetailAPIView(generics.RetrieveAPIView):
    serializer_class = ReservationSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Reservation.objects.select_related(
            "schedule",
            "schedule__train",
            "schedule__departure_station",
            "schedule__arrival_station",
        ).filter(user=self.request.user)


    