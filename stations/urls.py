from django.urls import path

from .views import StationListAPIView , StationCreateAPIView, StationDetailAPIView

urlpatterns = [
    # Stations
    path(
        "",
        StationListAPIView.as_view(),
        name="station-list",
    ),
    path(
        "/create",
        StationCreateAPIView.as_view(),
        name="station-create",
    ),
    path(
        "/<uuid:pk>",
        StationDetailAPIView.as_view(),
        name="station-detail",
    ),

]