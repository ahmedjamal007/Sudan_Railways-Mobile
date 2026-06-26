from django.contrib.auth.models import User
from django.contrib.auth import authenticate

from rest_framework import serializers

from .models import UserProfile


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = [
            "phone_number",
            "national_id",
            "gender",
            "profile_photo",
            "national_id_photo",
            "is_verified",
        ]
        read_only_fields = ["is_verified"]

class UserSerializer(serializers.ModelSerializer):
    profile = UserProfileSerializer()

    class Meta:
        model = User
        fields = [
            "id",
            "username",
            "first_name",
            "last_name",
            "email",
            "profile",
        ]

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, min_length=8)

    # profile fields
    phone_number = serializers.CharField(write_only=True)
    national_id = serializers.CharField(write_only=True)
    gender = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = [
            "username",
            "email",
            "password",
            "first_name",
            "last_name",
            "phone_number",
            "national_id",
            "gender",
        ]

    def create(self, validated_data):
        phone_number = validated_data.pop("phone_number")
        national_id = validated_data.pop("national_id")
        gender = validated_data.pop("gender")

        user = User.objects.create_user(
            username=validated_data["username"],
            email=validated_data["email"],
            password=validated_data["password"],
            first_name=validated_data.get("first_name", ""),
            last_name=validated_data.get("last_name", ""),
        )

        # create profile automatically
        UserProfile.objects.create(
            user=user,
            phone_number=phone_number,
            national_id=national_id,
            gender=gender,
        )

        return user
    
class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self, attrs):
        user = authenticate(
            username=attrs["username"],
            password=attrs["password"]
        )

        if not user:
            raise serializers.ValidationError("Invalid credentials")

        if not user.is_active:
            raise serializers.ValidationError("User is inactive")

        attrs["user"] = user
        return attrs
    
class ProfileUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = [
            "phone_number",
            "gender",
            "profile_photo",
            "national_id_photo",
        ]