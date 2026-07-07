from django.urls import path
from .views import (
    ImageUploadView,
    PolygonCreateView,
    PolygonListView,
    PolygonDeleteView,
)

urlpatterns = [
    path("upload/", ImageUploadView.as_view()),
    path("polygon/", PolygonCreateView.as_view(), name="polygon-create",),
    path("polygon/", PolygonListCreateView.as_view()),

    # DELETE polygon
    path("polygon/<int:pk>/", PolygonDeleteView.as_view()),
]