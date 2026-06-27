from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, IsAdminUser

from .models import  Schedule
from .serializers import ScheduleSerializer




class ScheduleListAPIView(generics.ListAPIView):
    queryset = (
        Schedule.objects
        .select_related(
            "train",
            "departure_station",
            "arrival_station",
        )
        .all()
    )

    serializer_class = ScheduleSerializer
    permission_classes = [IsAuthenticated]

class ScheduleCreateAPIView(generics.CreateAPIView):
    queryset = Schedule.objects.all()
    serializer_class = ScheduleSerializer
    permission_classes = [IsAdminUser]

class ScheduleDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Schedule.objects.select_related(
        "train",
        "departure_station",
        "arrival_station",
    )

    serializer_class = ScheduleSerializer
    permission_classes = [IsAdminUser]