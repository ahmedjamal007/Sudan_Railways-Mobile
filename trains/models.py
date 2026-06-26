import uuid
from django.db import models


class TrainStatus(models.TextChoices):
    ACTIVE = "ACTIVE", "Active"
    INACTIVE = "INACTIVE", "Inactive"


class TrainType(models.TextChoices):
    PASSENGER = "PASSENGER", "Passenger"
    EXPRESS = "EXPRESS", "Express"
    FREIGHT = "FREIGHT", "Freight"


class Train(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    train_number = models.CharField(max_length=20, unique=True)
    name = models.CharField(max_length=100)

    capacity = models.PositiveIntegerField()

    train_type = models.CharField(
        max_length=20,
        choices=TrainType.choices,
        default=TrainType.PASSENGER
    )

    status = models.CharField(
        max_length=20,
        choices=TrainStatus.choices,
        default=TrainStatus.ACTIVE
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "trains"
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.train_number} - {self.name}"