from django.shortcuts import render
from .models import Station
from .serializers import StationSerializer
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, IsAdminUser
# Create your views here.
class StationListAPIView(generics.ListAPIView):
    queryset = Station.objects.filter(is_active=True)
    serializer_class = StationSerializer
    permission_classes = [IsAuthenticated]


class StationCreateAPIView(generics.CreateAPIView):
    queryset = Station.objects.all()
    serializer_class = StationSerializer
    permission_classes = [IsAdminUser]

class StationDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Station.objects.all()
    serializer_class = StationSerializer
    permission_classes = [IsAdminUser]
