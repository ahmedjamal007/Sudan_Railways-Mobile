import uuid
from django.contrib.auth.models import User
from django.db import models


class Gender(models.TextChoices):
    MALE = "MALE", "Male"
    FEMALE = "FEMALE", "Female"


def profile_upload_path(instance, filename):
    return f"users/{instance.user.id}/profile/{filename}"


def national_id_upload_path(instance, filename):
    return f"users/{instance.user.id}/national_id/{filename}"


class UserProfile(models.Model):


    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name="profile"
    )

    phone_number = models.CharField(max_length=20)

    national_id = models.CharField(max_length=30, unique=True)

    gender = models.CharField(
        max_length=10,
        choices=Gender.choices
    )

    profile_photo = models.ImageField(
        upload_to=profile_upload_path,
        blank=True,
        null=True
    )

    national_id_photo = models.FileField(
        upload_to=national_id_upload_path,
        blank=True,
        null=True
    )

    is_verified = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.username