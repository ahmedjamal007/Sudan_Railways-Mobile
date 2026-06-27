import uuid

from django.db import models

from reservations.models import Reservation


class TicketStatus(models.TextChoices):
    ACTIVE = "ACTIVE", "Active"
    USED = "USED", "Used"
    CANCELLED = "CANCELLED", "Cancelled"


class Ticket(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )

    reservation = models.OneToOneField(
        Reservation,
        on_delete=models.CASCADE,
        related_name="ticket"
    )

    ticket_number = models.CharField(
        max_length=30,
        unique=True
    )

    status = models.CharField(
        max_length=20,
        choices=TicketStatus.choices,
        default=TicketStatus.ACTIVE
    )

    issued_at = models.DateTimeField(
        auto_now_add=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    class Meta:
        db_table = "tickets"
        ordering = ["-issued_at"]

    def __str__(self):
        return self.ticket_number