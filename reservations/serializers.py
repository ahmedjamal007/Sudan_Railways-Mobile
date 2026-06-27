from django.utils import timezone

from rest_framework import serializers

from .models import Reservation, ReservationStatus
from schedules.models import Schedule, ScheduleStatus


class ReservationSerializer(serializers.ModelSerializer):
    train_name = serializers.CharField(
        source="schedule.train.name",
        read_only=True
    )

    departure_station = serializers.CharField(
        source="schedule.departure_station.name",
        read_only=True
    )

    arrival_station = serializers.CharField(
        source="schedule.arrival_station.name",
        read_only=True
    )

    departure_datetime = serializers.DateTimeField(
        source="schedule.departure_datetime",
        read_only=True
    )

    class Meta:
        model = Reservation
        fields = [
            "id",
            "schedule",
            "train_name",
            "departure_station",
            "arrival_station",
            "departure_datetime",
            "seats",
            "total_price",
            "status",
            "created_at",
        ]
        read_only_fields = (
            "total_price",
            "status",
            "created_at",
        )

    def validate(self, attrs):
        schedule = attrs["schedule"]
        seats = attrs["seats"]

        if schedule.status != ScheduleStatus.AVAILABLE:
            raise serializers.ValidationError(
                "This schedule is not available."
            )

        if schedule.departure_datetime <= timezone.now():
            raise serializers.ValidationError(
                "This train has already departed."
            )

        if seats <= 0:
            raise serializers.ValidationError(
                "Seats must be greater than zero."
            )

        if seats > schedule.available_seats:
            raise serializers.ValidationError(
                "Not enough available seats."
            )

        return attrs

    def create(self, validated_data):
        schedule = validated_data["schedule"]
        seats = validated_data["seats"]

        reservation = Reservation.objects.create(
            user=self.context["request"].user,
            schedule=schedule,
            seats=seats,
            total_price=schedule.ticket_price * seats,
            status=ReservationStatus.PENDING_PAYMENT,
        )

        # Reduce available seats
        schedule.available_seats -= seats
        schedule.save(update_fields=["available_seats"])

        return reservation