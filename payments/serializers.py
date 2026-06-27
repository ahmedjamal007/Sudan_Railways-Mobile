from rest_framework import serializers

from .models import Payment
from reservations.models import Reservation, ReservationStatus


class PaymentSerializer(serializers.ModelSerializer):
    reservation_info = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Payment
        fields = [
            "id",
            "reservation",
            "reservation_info",
            "receipt",
            "status",
            "admin_note",
            "reviewed_at",
            "created_at",
            "updated_at",
        ]

        read_only_fields = [
            "status",
            "admin_note",
            "reviewed_at",
            "created_at",
            "updated_at",
        ]

    def get_reservation_info(self, obj):
        return {
            "id": str(obj.reservation.id),
            "train": obj.reservation.schedule.train.name,
            "departure_station": obj.reservation.schedule.departure_station.name,
            "arrival_station": obj.reservation.schedule.arrival_station.name,
            "departure_datetime": obj.reservation.schedule.departure_datetime,
            "total_price": obj.reservation.total_price,
        }

    def validate_reservation(self, reservation):
        request = self.context["request"]

        # Reservation must belong to the logged-in user
        if reservation.user != request.user:
            raise serializers.ValidationError(
                "This reservation does not belong to you."
            )

        # Reservation must be waiting for payment
        if reservation.status != ReservationStatus.PENDING_PAYMENT:
            raise serializers.ValidationError(
                "This reservation cannot receive a payment."
            )

        # Prevent duplicate payments
        if Payment.objects.filter(reservation=reservation).exists():
            raise serializers.ValidationError(
                "Payment has already been submitted."
            )

        return reservation

    def create(self, validated_data):
        payment = Payment.objects.create(**validated_data)

        reservation = payment.reservation
        reservation.status = ReservationStatus.PAYMENT_SUBMITTED
        reservation.save(update_fields=["status"])

        return payment