from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from .models import Ticket
from .serializers import TicketSerializer


class TicketListAPIView(generics.ListAPIView):
    serializer_class = TicketSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return (
            Ticket.objects
            .select_related(
                "reservation",
                "reservation__user",
                "reservation__schedule",
                "reservation__schedule__train",
                "reservation__schedule__departure_station",
                "reservation__schedule__arrival_station",
            )
            .filter(reservation__user=self.request.user)
            .order_by("-issued_at")
        )


class TicketDetailAPIView(generics.RetrieveAPIView):
    serializer_class = TicketSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return (
            Ticket.objects
            .select_related(
                "reservation",
                "reservation__user",
                "reservation__schedule",
                "reservation__schedule__train",
                "reservation__schedule__departure_station",
                "reservation__schedule__arrival_station",
            )
            .filter(reservation__user=self.request.user)
        )