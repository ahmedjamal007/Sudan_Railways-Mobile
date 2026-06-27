from django.db import models
import uuid

# Create your models here.

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