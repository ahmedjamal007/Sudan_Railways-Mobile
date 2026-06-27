from rest_framework import serializers

from .models import Schedule




class ScheduleSerializer(serializers.ModelSerializer):
    train_name = serializers.CharField(
        source="train.name",
        read_only=True
    )

    departure_station_name = serializers.CharField(
        source="departure_station.name",
        read_only=True
    )

    arrival_station_name = serializers.CharField(
        source="arrival_station.name",
        read_only=True
    )

    class Meta:
        model = Schedule
        fields = [
            "id",
            "train",
            "train_name",
            "departure_station",
            "departure_station_name",
            "arrival_station",
            "arrival_station_name",
            "departure_datetime",
            "arrival_datetime",
            "ticket_price",
            "available_seats",
            "status",
            "created_at",
            "updated_at",
        ]