import uuid

from django.db import models

from trains.models import Train


class Station(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )

    name = models.CharField(
        max_length=100,
        unique=True
    )

    code = models.CharField(
        max_length=10,
        unique=True
    )

    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name
    
class ScheduleStatus(models.TextChoices):
    AVAILABLE = "AVAILABLE", "Available"
    CANCELLED = "CANCELLED", "Cancelled"
    COMPLETED = "COMPLETED", "Completed"


class Schedule(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )

    train = models.ForeignKey(
        Train,
        on_delete=models.CASCADE,
        related_name="schedules"
    )

    departure_station = models.ForeignKey(
        Station,
        on_delete=models.PROTECT,
        related_name="departures"
    )

    arrival_station = models.ForeignKey(
        Station,
        on_delete=models.PROTECT,
        related_name="arrivals"
    )

    departure_datetime = models.DateTimeField()

    arrival_datetime = models.DateTimeField()

    ticket_price = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    available_seats = models.PositiveIntegerField()

    status = models.CharField(
        max_length=20,
        choices=ScheduleStatus.choices,
        default=ScheduleStatus.AVAILABLE
    )

    created_at = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["departure_datetime"]

    def __str__(self):
        return (
            f"{self.train.name} | "
            f"{self.departure_station} → "
            f"{self.arrival_station}"
        )
