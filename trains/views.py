from rest_framework import generics, permissions
from .models import Train
from .serializers import TrainSerializer


class TrainListCreateView(generics.ListCreateAPIView):
    queryset = Train.objects.all()
    serializer_class = TrainSerializer

    def get_permissions(self):
        if self.request.method == "POST":
            return [permissions.IsAdminUser()]
        return [permissions.IsAuthenticated()]
    


class TrainDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Train.objects.all()
    serializer_class = TrainSerializer

    def get_permissions(self):
        if self.request.method in ["PUT", "PATCH", "DELETE"]:
            return [permissions.IsAdminUser()]
        return [permissions.IsAuthenticated()]