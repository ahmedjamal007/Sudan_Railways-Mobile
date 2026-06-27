import uuid

from django.conf import settings
from django.db import models

from schedules.models import Schedule


class ReservationStatus(models.TextChoices):
    PENDING_PAYMENT = "PENDING_PAYMENT", "Pending Payment"
    PAYMENT_SUBMITTED = "PAYMENT_SUBMITTED", "Payment Submitted"
    CONFIRMED = "CONFIRMED", "Confirmed"
    CANCELLED = "CANCELLED", "Cancelled"


class Reservation(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
    )

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="reservations",
    )

    schedule = models.ForeignKey(
        Schedule,
        on_delete=models.PROTECT,
        related_name="reservations",
    )

    seats = models.PositiveIntegerField(default=1)

    total_price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
    )

    status = models.CharField(
        max_length=25,
        choices=ReservationStatus.choices,
        default=ReservationStatus.PENDING_PAYMENT,
    )

    notes = models.TextField(
        blank=True,
        null=True,
    )

    created_at = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.user.username} - {self.schedule}"