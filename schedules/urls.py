from django.urls import path

from .views import (
    ScheduleListAPIView,
    ScheduleCreateAPIView,
    ScheduleDetailAPIView,
)

urlpatterns = [
    # Stations
    # Schedules
    path(
        "",
        ScheduleListAPIView.as_view(),
        name="schedule-list",
    ),
    path(
        "create/",
        ScheduleCreateAPIView.as_view(),
        name="schedule-create",
    ),
    path(
        "<uuid:pk>/",
        ScheduleDetailAPIView.as_view(),
        name="schedule-detail",
    ),
]