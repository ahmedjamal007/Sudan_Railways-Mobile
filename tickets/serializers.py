from rest_framework import serializers

from .models import Ticket


class TicketSerializer(serializers.ModelSerializer):
    reservation_id = serializers.UUIDField(
        source="reservation.id",
        read_only=True
    )

    passenger = serializers.CharField(
        source="reservation.user.get_full_name",
        read_only=True
    )

    username = serializers.CharField(
        source="reservation.user.username",
        read_only=True
    )

    train = serializers.CharField(
        source="reservation.schedule.train.name",
        read_only=True
    )

    departure_station = serializers.CharField(
        source="reservation.schedule.departure_station.name",
        read_only=True
    )

    arrival_station = serializers.CharField(
        source="reservation.schedule.arrival_station.name",
        read_only=True
    )

    departure_datetime = serializers.DateTimeField(
        source="reservation.schedule.departure_datetime",
        read_only=True
    )

    arrival_datetime = serializers.DateTimeField(
        source="reservation.schedule.arrival_datetime",
        read_only=True
    )

    seats = serializers.IntegerField(
        source="reservation.seats",
        read_only=True
    )

    total_price = serializers.DecimalField(
        source="reservation.total_price",
        max_digits=10,
        decimal_places=2,
        read_only=True
    )

    class Meta:
        model = Ticket
        fields = [
            "id",
            "ticket_number",
            "reservation_id",
            "passenger",
            "username",
            "train",
            "departure_station",
            "arrival_station",
            "departure_datetime",
            "arrival_datetime",
            "seats",
            "total_price",
            "status",
            "issued_at",
        ]

        read_only_fields = fields